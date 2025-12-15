# File: benchmark_suite/benchmark.py
import time
import sys
import os
import json
import statistics

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_engine.protocols import DiffieHellmanProtocol, ECDHProtocol
from crypto_engine.elliptic_curve import EllipticCurve
import benchmark_suite.standard_params as params


def measure_execution(func, iterations=10):
    """Executes a function multiple times and returns mean and stdev."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append(end - start)

    return statistics.mean(times), statistics.stdev(times)


def run_suite():
    results = []

    print("--- Başlatılıyor: Kriptografik Performans Ölçümü ---", file=sys.stderr)

    # --- Test 1: DH-2048 (Group 14) ---
    def dh_2048_keygen():
        return DiffieHellmanProtocol(params.DH_2048_P, params.DH_2048_G)

    # Pre-generate arda for Handshake test
    arda_dh_2048 = dh_2048_keygen()
    burak_dh_2048_pub = dh_2048_keygen().public_key

    def dh_2048_handshake():
        arda_dh_2048.generate_shared_secret(burak_dh_2048_pub)

    # --- Test 2: ECDH-256 (NIST P-256) ---
    # Equivalent to 3072-bit RSA/DH security (approx 128-bit security level)
    curve_256 = EllipticCurve(params.NIST_P256_PARAMS['a'], params.NIST_P256_PARAMS['b'], params.NIST_P256_PARAMS['p'])
    G_256 = (params.NIST_P256_PARAMS['gx'], params.NIST_P256_PARAMS['gy'])
    n_256 = params.NIST_P256_PARAMS['n']

    def ecdh_256_keygen():
        return ECDHProtocol(curve_256, G_256, n_256)

    arda_ecdh_256 = ecdh_256_keygen()
    burak_ecdh_256_pub = ecdh_256_keygen().public_key

    def ecdh_256_handshake():
        arda_ecdh_256.generate_shared_secret(burak_ecdh_256_pub)

    # --- Test 3: DH-3072 (Group 15) ---
    def dh_3072_keygen():
        return DiffieHellmanProtocol(params.DH_3072_P, params.DH_3072_G)

    arda_dh_3072 = dh_3072_keygen()
    burak_dh_3072_pub = dh_3072_keygen().public_key

    def dh_3072_handshake():
        arda_dh_3072.generate_shared_secret(burak_dh_3072_pub)

    # --- Execution & Collection ---
    scenarios = [
        ("DH-2048", dh_2048_keygen, dh_2048_handshake, 2048 / 8),
        ("ECDH-256", ecdh_256_keygen, ecdh_256_handshake, 256 / 8 * 2),  # Approx point size
        ("DH-3072", dh_3072_keygen, dh_3072_handshake, 3072 / 8),
    ]

    for name, keygen_func, handshake_func, size_bytes in scenarios:
        print(f"Benchmarking {name}...", file=sys.stderr)
        kg_mean, kg_std = measure_execution(keygen_func)
        hs_mean, hs_std = measure_execution(handshake_func)

        results.append({
            "algorithm": name,
            "keygen_avg_sec": kg_mean,
            "keygen_std_sec": kg_std,
            "handshake_avg_sec": hs_mean,
            "handshake_std_sec": hs_std,
            "payload_bytes": int(size_bytes)
        })

    # Dump JSON to stdout for piping
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    run_suite()