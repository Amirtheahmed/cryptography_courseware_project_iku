import time
import sys
import os

# Üst dizindeki modülleri görebilmek için path ayarı
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_engine.protocols import DiffieHellmanProtocol, ECDHProtocol
from crypto_engine.elliptic_curve import EllipticCurve
import benchmark_suite.standard_params as params


def benchmark_dh(name, p, g, iterations=5):
    """Classic DH Performans Ölçümü"""
    print(f"\n--- {name} Benchmark Başlıyor ({iterations} iterasyon) ---")

    total_keygen_time = 0
    total_handshake_time = 0
    pub_key_size = 0

    for _ in range(iterations):
        # 1. Key Generation (Alice)
        start = time.time()
        alice = DiffieHellmanProtocol(p, g)
        end = time.time()
        total_keygen_time += (end - start)

        # Bob KeyGen (Ölçüme dahil değil ama gerekli)
        bob = DiffieHellmanProtocol(p, g)

        # 2. Shared Secret (Handshake)
        start = time.time()
        _ = alice.generate_shared_secret(bob.public_key)
        end = time.time()
        total_handshake_time += (end - start)

        # 3. Payload Size (Bytes)
        # Public Key (int) byte uzunluğu: (bit_length + 7) // 8
        pub_key_size = (alice.public_key.bit_length() + 7) // 8

    avg_keygen = total_keygen_time / iterations
    avg_handshake = total_handshake_time / iterations

    return avg_keygen, avg_handshake, pub_key_size


def benchmark_ecdh(name, ec_params, iterations=5):
    """ECDH Performans Ölçümü"""
    if ec_params['p'] == 0:
        print(f"\n--- {name} Benchmark Atlanıyor (Placeholder Parametreler) ---")
        return 0, 0, 0

    print(f"\n--- {name} Benchmark Başlıyor ({iterations} iterasyon) ---")

    curve = EllipticCurve(ec_params['a'], ec_params['b'], ec_params['p'])
    G = (ec_params['gx'], ec_params['gy'])
    n = ec_params['n']

    total_keygen_time = 0
    total_handshake_time = 0
    pub_key_size = 0

    for _ in range(iterations):
        # 1. Key Generation (Alice)
        start = time.time()
        alice = ECDHProtocol(curve, G, n)
        end = time.time()
        total_keygen_time += (end - start)

        bob = ECDHProtocol(curve, G, n)

        # 2. Shared Secret (Handshake)
        start = time.time()
        _ = alice.generate_shared_secret(bob.public_key)
        end = time.time()
        total_handshake_time += (end - start)

        # 3. Payload Size (Bytes) - Uncompressed Point (04 || x || y)
        # x ve y koordinatlarının her biri (p_bits + 7) // 8 byte
        coord_bytes = (ec_params['p'].bit_length() + 7) // 8
        pub_key_size = 1 + (2 * coord_bytes)  # 1 byte prefix + x + y

    avg_keygen = total_keygen_time / iterations
    avg_handshake = total_handshake_time / iterations

    return avg_keygen, avg_handshake, pub_key_size


if __name__ == "__main__":
    print("Algorithm,Avg_KeyGen_Time(s),Avg_Handshake_Time(s),PublicKey_Size(Bytes)")

    # 1. Test: DH-2048
    kg, hs, size = benchmark_dh("DH-2048", params.DH_2048_P, params.DH_2048_G)
    print(f"DH-2048: {kg:.5f}, {hs:.5f}, {size}")

    # 2. Test: ECDH-256 (NIST P-256) -> DH-3072 seviyesine yakındır güvenlik olarak
    kg, hs, size = benchmark_ecdh("ECDH-P256", params.NIST_P256_PARAMS)
    print(f"ECDH-P256: {kg:.5f}, {hs:.5f}, {size}")

    # 3. Test: DH-3072
    kg, hs, size = benchmark_dh("DH-3072", params.DH_3072_P, params.DH_3072_G)
    print(f"DH-3072: {kg:.5f}, {hs:.5f}, {size}")

    # 4. Test: ECDH-384 (NIST P-384)
    kg, hs, size = benchmark_ecdh("ECDH-P384", params.NIST_P384_PARAMS)
    print(f"ECDH-P384: {kg:.5f}, {hs:.5f}, {size}")