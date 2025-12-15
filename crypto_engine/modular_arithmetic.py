import random
"""
### Teknik Açıklama

**Neden `pow()` yerine `square_and_multiply` kullandık?**

Diffie-Hellman güvenliği, Ayrık Logaritma Probleminin (Discrete Logarithm Problem) zorluğuna dayanır: g^a mod p hesaplamak kolaydır, ancak sonuçtan a'yı bulmak zordur.

Eğer a sayısı 2048-bitlik bir sayı ise, değeri yaklaşık 10^617'dir. Eğer bu işlemi "üs kadar çarpma" (naive approach) yaparak hesaplamaya çalışsaydık, evrenin yaşından daha uzun sürerdi.

**Square-and-Multiply**, üssü ikilik tabana çevirerek işlem sayısını sayının bit uzunluğuna (örneğin 2048 adım) indirir.
*   **Örnek:** 3^5 (mod 100)
*   Naive: 3 * 3 * 3 * 3 * 3 (4 çarpma)
*   S&M (5 = 101 binary):
    1.  Bit '1': Kare + Çarp -> 1^2 * 3 = 3
    2.  Bit '0': Kare -> 3^2 = 9
    3.  Bit '1': Kare + Çarp -> 9^2 * 3 = 81 * 3 = 243 ≅ 43 (mod 100)
*   Büyük sayılarda bu fark devasa performans kazancı sağlar ve DH'yi uygulanabilir kılar.
"""

class ModularArithmetic:
    """
    Klasik Diffie-Hellman (DH) için temel matematiksel operasyonları içerir.
    Python'ın built-in pow() fonksiyonunu KULLANMAZ.
    """

    @staticmethod
    def square_and_multiply(base: int, exponent: int, modulus: int) -> int:
        """
        Hesaplar: (base ^ exponent) % modulus
        Algoritma: Square-and-Multiply
        Karmaşıklık: O(log exponent) - Büyük sayılarla çalışmak için zorunludur.
        """
        if modulus == 1:
            return 0

        result = 1
        # Üssü ikilik tabana (binary) çeviriyoruz (örn: 5 -> '101')
        # '0b' öneki olmadan string olarak alıyoruz
        binary_exponent = bin(exponent)[2:]

        for bit in binary_exponent:
            # Adım 1: Square (Kare Al)
            result = (result * result) % modulus

            # Adım 2: Multiply (Eğer bit 1 ise Çarp)
            if bit == '1':
                result = (result * base) % modulus

        return result

    @staticmethod
    def generate_prime_candidate(length: int) -> int:
        """
        Basit bir test amaçlı asal sayı adayı üretir (Miller-Rabin testi eklenebilir).
        Bu simülasyon için random büyük tek sayılar üretiyoruz.
        """
        p = random.getrandbits(length)
        # Sayının tek sayı olduğundan ve en yüksek bitin 1 olduğundan emin ol
        p |= (1 << length - 1) | 1
        return p

    @staticmethod
    def is_prime(n: int, k: int = 5) -> bool:
        """
        Miller-Rabin asallık testi.
        Büyük sayıların asallığını olasılıksal olarak test eder.
        """
        if n == 2 or n == 3: return True
        if n % 2 == 0: return False

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = ModularArithmetic.square_and_multiply(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = ModularArithmetic.square_and_multiply(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    @staticmethod
    def get_safe_prime(length: int) -> int:
        """
        Belirtilen bit uzunluğunda bir asal sayı döndürür.
        Gerçek dünya senaryosu için RFC 3526 grupları kullanılmalıdır,
        ancak burada matematiksel motoru test ediyoruz.
        """
        while True:
            p = ModularArithmetic.generate_prime_candidate(length)
            if ModularArithmetic.is_prime(p):
                return p
