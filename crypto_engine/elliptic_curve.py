from typing import Tuple, Optional

"""
### Teknik Açıklama ("The Why")

Bu kodda uyguladığımız prensipler neden önemli?

1.  **Double-and-Add Algoritması:**
    Tıpkı Klasik DH'deki *Square-and-Multiply* gibi, bu algoritma da işlemin logaritmik zamanda bitmesini sağlar.
    *   256-bitlik bir anahtar (k) için, eğer basit toplama yapsaydık ($P+P+P...$) $2^{256}$ işlem gerekirdi. Bu imkansızdır.
    *   **Double-and-Add** ile sadece yaklaşık **256 tane Point Doubling** ve ortalama **128 tane Point Addition** işlemiyle sonuca ulaşırız. ECDH'yi hızlı ve kullanılabilir kılan budur.

2.  **Modüler Ters (Modular Inverse):**
    Kodda `(y2 - y1) / (x2 - x1)` işlemi yapmamız gerekiyor. Ancak sonlu cisimlerde (Finite Fields) kesirli sayı yoktur.
    *   Örnek: Mod 17'de $4/2 = 2$ dir.
    *   Ancak $4 \times (2^{-1}) \pmod{17}$ olarak hesaplarız.
    *   `_modular_inverse` fonksiyonumuz, Genişletilmiş Öklid algoritmasını kullanarak bu "bölme" işlemini gerçekleştirir. Bu fonksiyon olmadan eğri üzerinde hareket edemezdik.

3.  **Point at Infinity (`None`):**
    Normal sayılarda `0` neyse, Elliptik Eğrilerde "Sonsuzdaki Nokta" odur. Birim elemandır. Kodda bunu `None` olarak temsil ettik ve `point_add` fonksiyonunun başında bu durumu (Identity) özel olarak ele aldık.
"""

# Noktayı temsil etmek için basit bir tip tanımı: (x, y) veya None (Sonsuzdaki Nokta)
Point = Optional[Tuple[int, int]]


class EllipticCurve:
    """
    Weierstrass formundaki elliptik eğriler üzerinde işlemleri gerçekleştirir:
    y^2 = x^3 + ax + b (mod p)

    Kütüphane kullanmadan 'Double-and-Add' algoritmasını uygular.
    """

    def __init__(self, a: int, b: int, p: int):
        self.a = a
        self.b = b
        self.p = p

    def _modular_inverse(self, n: int) -> int:
        """
        Genişletilmiş Öklid Algoritması (Extended Euclidean Algorithm).
        Mod p'de n'in çarpımsal tersini bulur.
        Yani: (n * x) % p == 1 olan x'i bulur.
        Bu işlem, eğim hesaplarken bölme işlemi yerine kullanılır.
        """
        if n == 0:
            raise ValueError("0'ın tersi yoktur (Sıfıra bölme hatası).")

        n = n % self.p
        original_p = self.p
        x0, x1 = 0, 1

        if self.p == 1: return 0

        temp_n = n
        temp_p = self.p

        while temp_n > 1:
            # Standart öklid algoritması adımları
            q = temp_n // temp_p
            temp_n, temp_p = temp_p, temp_n % temp_p
            x0, x1 = x1 - q * x0, x0

        if x1 < 0:
            x1 += original_p

        return x1

    def point_add(self, P: Point, Q: Point) -> Point:
        """
        İki noktayı toplar: P + Q
        Geometrik olarak: P ve Q'dan geçen doğrunun eğriyi kestiği 3. noktanın x eksenine göre yansıması.
        """
        # 1. Durum: Birim eleman (Sonsuzdaki Nokta - 0) ile toplama
        if P is None: return Q
        if Q is None: return P

        x1, y1 = P
        x2, y2 = Q

        # 2. Durum: Nokta tersi ile toplama (P + (-P) = 0)
        # Dikey bir doğru oluşur, sonsuza gider.
        if x1 == x2 and y1 != y2:
            return None

        # 3. Durum: Nokta kendisiyle toplanıyorsa (P == Q) -> Point Doubling
        if x1 == x2 and y1 == y2:
            return self.point_double(P)

        # 4. Durum: Genel Toplama (P != Q)
        # Eğim (m) = (y2 - y1) / (x2 - x1) mod p
        # Bölme işlemi modüler ters ile çarpmaya dönüşür.
        numerator = (y2 - y1) % self.p
        denominator = (x2 - x1) % self.p

        inv_denom = self._modular_inverse(denominator)
        slope = (numerator * inv_denom) % self.p

        # Yeni koordinatları hesapla
        x3 = (slope * slope - x1 - x2) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def point_double(self, P: Point) -> Point:
        """
        Bir noktayı kendisiyle toplar: P + P = 2P
        Geometrik olarak: P noktasındaki teğetin eğimi kullanılır.
        """
        if P is None: return None

        x1, y1 = P

        # Eğer y1 = 0 ise teğet dikeydir -> Sonsuz
        if y1 == 0:
            return None

        # Eğim (m) = (3x^2 + a) / (2y) mod p
        numerator = (3 * x1 * x1 + self.a) % self.p
        denominator = (2 * y1) % self.p

        inv_denom = self._modular_inverse(denominator)
        slope = (numerator * inv_denom) % self.p

        x3 = (slope * slope - 2 * x1) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def scalar_multiply(self, k: int, P: Point) -> Point:
        """
        Hesaplar: k * P (P noktasını k kere kendisiyle topla)
        Algoritma: Double-and-Add
        Karmaşıklık: O(log k)

        ECDH'de "Public Key" üretimi ve "Shared Secret" hesaplaması burada yapılır.
        k: Private Key (Scalar)
        P: Generator Point
        Sonuç: Public Key (Point)
        """
        result = None  # Başlangıçta 0 (Sonsuzdaki Nokta)
        addend = P

        # Scalar (k) bit bit işlenir
        while k > 0:
            # Eğer son bit 1 ise, mevcut 'addend' değerini sonuca ekle
            if k & 1:
                result = self.point_add(result, addend)

            # Addend'i iki katına çıkar (Double)
            addend = self.point_double(addend)

            # Bir sonraki bite geç
            k >>= 1

        return result