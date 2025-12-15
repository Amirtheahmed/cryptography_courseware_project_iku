import time
import sys
import os
import json
import statistics
from dataclasses import dataclass

# Ensure we can import from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_engine.protocols import DiffieHellmanProtocol, ECDHProtocol
from crypto_engine.elliptic_curve import EllipticCurve
import benchmark_suite.standard_params as params

# CONFIGURATION
ITERATIONS_FAST = 50  # For ECDH and DH-2048
ITERATIONS_SLOW = 10  # For DH-3072 (It is very slow on limited CPUs)
WARMUP_ROUNDS = 5  # Prime the CPU cache/Interpreter


@dataclass
class BenchmarkResult:
    algorithm: str
    operation: str
    avg_time_ms: float
    ops_per_sec: float
    stdev_ms: float
    payload_bytes: int


class BenchmarkRunner:
    def __init__(self):
        self.results = []
        print(f"{'=' * 60}", file=sys.stderr)
        print(f"BENCHMARK SUITE: Diffie-Hellman vs. ECDHE", file=sys.stderr)
        print(f"Environment: Python {sys.version.split()[0]}", file=sys.stderr)
        print(f"{'=' * 60}\n", file=sys.stderr)

    def _print_progress(self, algo, op, current, total):
        """Prints a visual progress bar to stderr."""
        percent = 100 * (current / total)
        bar_len = 30
        filled_len = int(bar_len * current // total)
        bar = '█' * filled_len + '-' * (bar_len - filled_len)
        sys.stderr.write(f'\rBenchmarking {algo} [{op}]: |{bar}| {percent:.1f}%')
        sys.stderr.flush()

    def measure(self, name, operation_name, func, iterations, payload_size):
        """
        Runs the benchmark with warm-up rounds and statistical analysis.
        """
        # 1. Warm-up (Ignore these results)
        for _ in range(WARMUP_ROUNDS):
            func()

        # 2. Actual Measurement
        times = []
        for i in range(iterations):
            self._print_progress(name, operation_name, i + 1, iterations)

            start = time.perf_counter()
            func()
            end = time.perf_counter()

            times.append(end - start)

        print("", file=sys.stderr)  # New line after progress bar

        # 3. Statistics
        avg_time = statistics.mean(times)
        stdev = statistics.stdev(times) if len(times) > 1 else 0.0
        ops_sec = 1.0 / avg_time if avg_time > 0 else 0.0

        result = BenchmarkResult(
            algorithm=name,
            operation=operation_name,
            avg_time_ms=avg_time * 1000,  # Convert to milliseconds for readability
            ops_per_sec=ops_sec,
            stdev_ms=stdev * 1000,
            payload_bytes=payload_size
        )
        self.results.append(result)

        # Print summary to console
        print(f"   -> Avg: {result.avg_time_ms:.2f} ms | Throughput: {result.ops_per_sec:.1f} ops/sec", file=sys.stderr)
        print(f"   -> Payload: {result.payload_bytes} bytes", file=sys.stderr)
        print("-" * 40, file=sys.stderr)

    def run(self):
        # --- SCENARIO 1: DH-2048 (Group 14) ---
        dh_2048_p = params.DH_2048_P
        dh_2048_g = params.DH_2048_G

        # Setup for Handshake Test (Pre-generate one party)
        alice_dh_2048 = DiffieHellmanProtocol(dh_2048_p, dh_2048_g)
        bob_dh_2048_pub = DiffieHellmanProtocol(dh_2048_p, dh_2048_g).public_key

        self.measure(
            "DH-2048", "KeyGen",
            lambda: DiffieHellmanProtocol(dh_2048_p, dh_2048_g),
            ITERATIONS_FAST, 256  # 2048 bits = 256 bytes
        )

        self.measure(
            "DH-2048", "Handshake",
            lambda: alice_dh_2048.generate_shared_secret(bob_dh_2048_pub),
            ITERATIONS_FAST, 256
        )

        # --- SCENARIO 2: ECDH-256 (NIST P-256) ---
        # 128-bit Security Level (Much stronger per bit than DH)
        curve = EllipticCurve(
            params.NIST_P256_PARAMS['a'],
            params.NIST_P256_PARAMS['b'],
            params.NIST_P256_PARAMS['p']
        )
        G = (params.NIST_P256_PARAMS['gx'], params.NIST_P256_PARAMS['gy'])
        n = params.NIST_P256_PARAMS['n']

        alice_ecdh = ECDHProtocol(curve, G, n)
        bob_ecdh_pub = ECDHProtocol(curve, G, n).public_key

        # ECDH Public key is (x, y). Each is 256 bits (32 bytes). Total ~64 bytes.
        self.measure(
            "ECDH-256", "KeyGen",
            lambda: ECDHProtocol(curve, G, n),
            ITERATIONS_FAST, 64
        )

        self.measure(
            "ECDH-256", "Handshake",
            lambda: alice_ecdh.generate_shared_secret(bob_ecdh_pub),
            ITERATIONS_FAST, 64
        )

        # --- SCENARIO 3: DH-3072 (Group 15) ---
        # 128-bit Security Level (Equivalent to ECDH-256)
        dh_3072_p = params.DH_3072_P
        dh_3072_g = params.DH_3072_G

        alice_dh_3072 = DiffieHellmanProtocol(dh_3072_p, dh_3072_g)
        bob_dh_3072_pub = DiffieHellmanProtocol(dh_3072_p, dh_3072_g).public_key

        self.measure(
            "DH-3072", "KeyGen",
            lambda: DiffieHellmanProtocol(dh_3072_p, dh_3072_g),
            ITERATIONS_SLOW, 384  # 3072 bits = 384 bytes
        )

        self.measure(
            "DH-3072", "Handshake",
            lambda: alice_dh_3072.generate_shared_secret(bob_dh_3072_pub),
            ITERATIONS_SLOW, 384
        )

        # Output JSON to stdout (for report generator pipe)
        # We transform the data to match the Report Generator's expected format
        # We aggregate KeyGen and Handshake for the simple graph, or we can update the graph.
        # For compatibility with existing report generator, we merge them into one object per Algo.

        final_data = []
        algos = ["DH-2048", "ECDH-256", "DH-3072"]

        for algo in algos:
            keygen = next(r for r in self.results if r.algorithm == algo and r.operation == "KeyGen")
            handshake = next(r for r in self.results if r.algorithm == algo and r.operation == "Handshake")

            final_data.append({
                "algorithm": algo,
                "keygen_avg_sec": keygen.avg_time_ms / 1000.0,  # Convert back to seconds for compatibility
                "handshake_avg_sec": handshake.avg_time_ms / 1000.0,
                "payload_bytes": keygen.payload_bytes
            })

        print(json.dumps(final_data, indent=2))


if __name__ == "__main__":
    runner = BenchmarkRunner()
    runner.run()