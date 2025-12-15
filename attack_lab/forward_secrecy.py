import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_engine.protocols import DiffieHellmanProtocol
from benchmark_suite.standard_params import DH_2048_P, DH_2048_G
from attack_lab.utils import *


def run_forward_secrecy_demo():
    log_title("SCENARIO A: Forward Secrecy Analysis")

    # ==========================================
    # PART 1: THE STATIC KEY DISASTER
    # ==========================================
    print(f"{Colors.BOLD}--- Simulation 1: Static DH (No Forward Secrecy) ---{Colors.RESET}")

    # 1. Setup Static Server (burak uses Long Term Key)
    burak_static = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    log_actor("Server(burak)", "Initialized with STATIC Private Key", f"Key: {str(burak_static._private_key)[:10]}...")

    # 2. Simulate Past Traffic (Session 1 - Yesterday)
    arda_v1 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)  # arda is ephemeral

    # Handshake
    s1_secret = burak_static.generate_shared_secret(arda_v1.public_key)
    s1_msg = "My password is 'hunter2'"
    s1_cipher = simple_xor_encrypt(s1_msg, s1_secret)

    log_actor("arda", "Sent Encrypted Msg (Session 1)", f"Ciphertext: {s1_cipher.hex()[:20]}...", Colors.BLUE)

    # 3. Simulate Traffic (Session 2 - Today)
    arda_v2 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)

    # Handshake
    s2_secret = burak_static.generate_shared_secret(arda_v2.public_key)
    s2_msg = "Attack at dawn"
    s2_cipher = simple_xor_encrypt(s2_msg, s2_secret)

    log_actor("arda", "Sent Encrypted Msg (Session 2)", f"Ciphertext: {s2_cipher.hex()[:20]}...", Colors.BLUE)

    # 4. THE LEAK (Mallory hacks the server TODAY)
    leaked_private_key = burak_static._private_key
    log_attack("SERVER COMPROMISED!", f"Leaked Key: {str(leaked_private_key)[:10]}...")

    # 5. The Exploit (Time Travel)
    # Mallory uses the key stolen TODAY to decrypt Session 1 (YESTERDAY)
    print(f"\n{Colors.RED}Mallory attempts to decrypt PAST Session 1 logs...{Colors.RESET}")

    # Mallory reconstructs the secret: (arda_Public_V1 ^ Leaked_burak_Priv) % P
    mallory_s1_calc = pow(arda_v1.public_key, leaked_private_key, DH_2048_P)
    decrypted_s1 = simple_xor_decrypt(s1_cipher, mallory_s1_calc)

    if decrypted_s1 == s1_msg:
        log_attack("DECRYPTION SUCCESSFUL", f"Recovered Past Msg: '{decrypted_s1}'")
        print(f"{Colors.RED}>> CRITICAL FAILURE: Compromise of current key exposed past data.{Colors.RESET}\n")
    else:
        print("Decryption Failed.")

    # ==========================================
    # PART 2: THE EPHEMERAL FIX (DHE)
    # ==========================================
    print(f"{Colors.BOLD}--- Simulation 2: Ephemeral DH (Perfect Forward Secrecy) ---{Colors.RESET}")

    # 1. Session 1 (Yesterday) - burak uses Ephemeral Key A
    burak_eph_1 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    arda_eph_1 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    s1_secret = burak_eph_1.generate_shared_secret(arda_eph_1.public_key)
    s1_cipher = simple_xor_encrypt("Nuclear Launch Codes: 0000", s1_secret)

    log_actor("System", "Session 1 Complete", "Keys destroyed from memory.", Colors.YELLOW)

    # 2. Session 2 (Today) - burak uses Ephemeral Key B
    burak_eph_2 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)  # NEW KEY!
    arda_eph_2 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    s2_secret = burak_eph_2.generate_shared_secret(arda_eph_2.public_key)

    # 3. THE LEAK (Mallory hacks server TODAY)
    # She only gets the key currently in memory (Session 2's key)
    leaked_key_today = burak_eph_2._private_key
    log_attack("SERVER COMPROMISED!", f"Leaked Key (Session 2): {str(leaked_key_today)[:10]}...")

    # 4. The Exploit Attempt
    print(f"\n{Colors.RED}Mallory attempts to decrypt PAST Session 1 logs...{Colors.RESET}")

    # Mallory tries to use Today's key on Yesterday's traffic
    mallory_fail_calc = pow(arda_eph_1.public_key, leaked_key_today, DH_2048_P)
    decrypted_attempt = simple_xor_decrypt(s1_cipher, mallory_fail_calc)

    if decrypted_attempt != "Nuclear Launch Codes: 0000":
        print(f"{Colors.GREEN}{Colors.BOLD}>> DECRYPTION FAILED!{Colors.RESET}")
        print(f"   Garbage Output: {decrypted_attempt[:20]}...")
        log_actor("System", "Forward Secrecy Verified", "Past secrets remain secure.", Colors.GREEN)


if __name__ == "__main__":
    run_forward_secrecy_demo()