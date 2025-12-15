import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_engine.protocols import DiffieHellmanProtocol
from crypto_engine.modular_arithmetic import ModularArithmetic
from benchmark_suite.standard_params import DH_2048_P, DH_2048_G
from attack_lab.utils import *


class Naiveburak(DiffieHellmanProtocol):
    """
    A Vulnerable Implementation of burak.
    He forgot to check if the public key is in range [2, p-2].
    """

    def generate_shared_secret(self, other_public_key: int) -> int:
        # VULNERABILITY: No check for small subgroup attacks!
        # Normal code would raise Error if other_public_key == p-1

        # Just compute straight away
        shared_secret = ModularArithmetic.square_and_multiply(other_public_key, self._private_key, self.p)
        return shared_secret


def run_mitm_demo():
    log_title("SCENARIO B: Small Subgroup Confinement Attack")

    # 1. Setup
    p = DH_2048_P
    g = DH_2048_G

    # Naive burak is initialized
    burak = Naiveburak(p, g)
    log_actor("burak (Naive)", "Waiting for arda's Public Key...", "", Colors.GREEN)

    # 2. Mallory Intercepts
    log_actor("arda", "Sends Public Key A", "Points to -> burak", Colors.BLUE)
    log_attack("INTERCEPTION", "Mallory blocks arda's key.")

    # 3. Injection (The Attack)
    # Mallory sends p-1 (which is -1 mod p). This has Order 2.
    # The result will be (-1)^b.
    # If b is even -> 1. If b is odd -> p-1.
    malicious_key = p - 1
    log_attack("INJECTION", f"Mallory sends (P - 1) to burak.")

    # 4. burak Computes Shared Secret
    # burak thinks 'malicious_key' is arda.
    try:
        buraks_secret = burak.generate_shared_secret(malicious_key)
        log_actor("burak (Naive)", "Computes Shared Secret", f"Value: {str(buraks_secret)[:10]}... (Hidden)", Colors.GREEN)

        # burak encrypts sensitive data
        secret_msg = "Launch Missiles at 12:00"
        ciphertext = simple_xor_encrypt(secret_msg, buraks_secret)
        log_actor("burak (Naive)", "Sends Encrypted Data", f"Bytes: {ciphertext.hex()[:20]}...", Colors.GREEN)

    except ValueError as e:
        print("burak detected the attack! (This shouldn't happen in Naiveburak)")
        return

    # 5. Mallory Brute Forces
    print(f"\n{Colors.RED}Mallory starts Brute Force...{Colors.RESET}")
    log_actor("Mallory", "Analyzing Subgroup...", "Generator order is 2. Search space size: 2 keys.", Colors.RED)

    # There are only 2 possible secrets: 1 or p-1
    possible_keys = [1, p - 1]

    for candidate_key in possible_keys:
        print(f"  Trying Candidate Key: {str(candidate_key)[:10]}...", end=" ")

        # Attempt decrypt
        decrypted = simple_xor_decrypt(ciphertext, candidate_key)

        # Check if it looks like English text (simple heuristic)
        if "Missiles" in decrypted:
            print(f"{Colors.GREEN}[MATCH FOUND]{Colors.RESET}")
            log_attack("CRACKED", f"Message: '{decrypted}'")
            print(f"{Colors.RED}>> ATTACK SUCCESS: 2048-bit security reduced to 2 guesses.{Colors.RESET}")
            break
        else:
            print(f"{Colors.YELLOW}[FAIL]{Colors.RESET}")


if __name__ == "__main__":
    run_mitm_demo()