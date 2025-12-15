import sys
import hashlib


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'  # arda
    GREEN = '\033[92m'  # burak
    RED = '\033[91m'  # Mallory/Attacker
    YELLOW = '\033[93m'  # System/Info
    BOLD = '\033[1m'
    RESET = '\033[0m'


def log_title(title):
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== {title} ==={Colors.RESET}")
    print(f"{Colors.HEADER}{'=' * (len(title) + 8)}{Colors.RESET}\n")


def log_actor(name, action, detail="", color=Colors.RESET):
    print(f"{color}{Colors.BOLD}[{name}]{Colors.RESET} {action}")
    if detail:
        print(f"    {Colors.YELLOW}↳ {detail}{Colors.RESET}")


def log_attack(action, result):
    print(f"{Colors.RED}{Colors.BOLD}[ATTACK]{Colors.RESET} {action}")
    print(f"    {Colors.RED}↳ RESULT: {result}{Colors.RESET}")


def simple_xor_encrypt(message: str, shared_secret_int: int) -> bytes:
    """
    A toy encryption for demonstration.
    Hashes the integer shared secret to get a key, then XORs the message.
    """
    # 1. Derive a key from the shared secret integer
    key_hash = hashlib.sha256(str(shared_secret_int).encode()).digest()

    # 2. XOR encrypt
    msg_bytes = message.encode()
    encrypted = bytearray()
    for i, b in enumerate(msg_bytes):
        encrypted.append(b ^ key_hash[i % len(key_hash)])
    return bytes(encrypted)


def simple_xor_decrypt(ciphertext: bytes, shared_secret_int: int) -> str:
    """Decrypts the XOR message."""
    key_hash = hashlib.sha256(str(shared_secret_int).encode()).digest()
    decrypted = bytearray()
    for i, b in enumerate(ciphertext):
        decrypted.append(b ^ key_hash[i % len(key_hash)])
    return decrypted.decode('utf-8', errors='ignore')