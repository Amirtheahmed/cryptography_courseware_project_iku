import secrets
from typing import Optional, Tuple
from .modular_arithmetic import ModularArithmetic
from .elliptic_curve import EllipticCurve, Point

"""
### Teknik Açıklama ("The Why")

1.  **Ephemeral vs. Static:**
    *   Sınıflarımızda `private_key` parametresi opsiyoneldir.
    *   Eğer boş bırakılırsa (`None`), `secrets.randbelow()` kullanılarak her seferinde yeni bir anahtar üretilir. Bu **Ephemeral (Geçici)** anahtar değişimidir ve **Forward Secrecy (İleriye Dönük Gizlilik)** sağlar. Yani bir saldırgan gelecekte sunucuyu hacklese bile, geçmişte üretilen bu rastgele anahtarları bulamaz (çünkü silinmiştir).
    *   Eğer bir `private_key` verilirse, bu **Static** anahtar değişimidir. 3. Aşamada (Break Phase), statik anahtar kullanan bir sistemin geçmiş mesajlarının nasıl çözüldüğünü göstereceğiz.

2.  **Güvenlik Kontrolleri:**
    *   `DiffieHellmanProtocol` içinde `if other_public_key <= 1...` kontrolü ekledik. Bu, **Small Subgroup Confinement Attack** (Küçük Alt Grup Hapsetme Saldırısı) önlemidir. Saldırganın araya girip `1` veya `p-1` göndererek ortak sırrı tahmin edilebilir (1 veya -1) hale getirmesini engeller.
    *   3. Aşamada "Saf Bob" (Naive Bob) karakterini yaratırken bu kontrolleri bilerek kaldıracağız.

3.  **Performans Farkı (Teorik):**
    *   `DiffieHellmanProtocol` public key üretmek için 2048-bitlik bir üs alma işlemi yapar (`square_and_multiply`).
    *   `ECDHProtocol` ise 256-bitlik bir skaler çarpım yapar (`scalar_multiply`).
    *   Bir sonraki aşamada (Measure Phase), bu bit farkının (2048 vs 256) işlemci sürelerine nasıl yansıdığını ölçeceğiz.
"""

class DiffieHellmanProtocol:
    """
    Klasik Diffie-Hellman (DH) Protokolü.
    Hem Ephemeral (DHE) hem de Static DH senaryolarını destekler.
    """

    def __init__(self, p: int, g: int, private_key: Optional[int] = None):
        """
        :param p: Asal modül (Prime modulus)
        :param g: Üreteç (Generator)
        :param private_key: Eğer verilirse 'Static DH' olur, verilmezse rastgele üretilir (Ephemeral).
        """
        self.p = p
        self.g = g

        # Eğer özel anahtar verilmediyse, kriptografik olarak güvenli rastgele bir sayı üret (Ephemeral)
        # Aralık: [2, p-2]
        if private_key is None:
            self._private_key = 2 + secrets.randbelow(p - 3)
            self.is_ephemeral = True
        else:
            self._private_key = private_key
            self.is_ephemeral = False

        # Public Key Hesaplama: A = g^a mod p
        # Kendi yazdığımız Square-and-Multiply algoritmasını kullanıyoruz.
        self.public_key = ModularArithmetic.square_and_multiply(self.g, self._private_key, self.p)

    def generate_shared_secret(self, other_public_key: int) -> int:
        """
        Karşı tarafın Public Key'ini (B) kullanarak ortak sırrı hesaplar.
        S = B^a mod p
        """
        # Güvenlik Kontrolü: Gelen anahtarın 1 veya p-1 olup olmadığı kontrol edilmeli (Small Subgroup Attack)
        # Ancak "Break" aşamasında bu kontrolü bilerek yapmayan "Naive Bob" kullanacağız.
        # Bu sınıf güvenli versiyonu temsil etsin:
        if other_public_key <= 1 or other_public_key >= self.p - 1:
            raise ValueError("Gecersiz Public Key! (Small Subgroup Saldirisi Riski)")

        shared_secret = ModularArithmetic.square_and_multiply(other_public_key, self._private_key, self.p)
        return shared_secret


class ECDHProtocol:
    """
    Elliptic Curve Diffie-Hellman (ECDH) Protokolü.
    Daha küçük anahtar boyutlarıyla aynı güvenlik seviyesini sağlar.
    """

    def __init__(self, curve: EllipticCurve, G: Point, order_n: int, private_key: Optional[int] = None):
        """
        :param curve: EllipticCurve sınıfı örneği (y^2 = x^3 + ax + b)
        :param G: Başlangıç noktası (Generator Point)
        :param order_n: G noktasının mertebesi (Order of subgroup)
        :param private_key: Opsiyonel statik anahtar.
        """
        self.curve = curve
        self.G = G
        self.n = order_n

        # Private Key (d): [1, n-1] aralığında rastgele bir tam sayı
        if private_key is None:
            self._private_key = 1 + secrets.randbelow(self.n - 1)
            self.is_ephemeral = True
        else:
            self._private_key = private_key
            self.is_ephemeral = False

        # Public Key (Q): Q = d * G
        # Kendi yazdığımız Double-and-Add algoritmasını kullanıyoruz.
        self.public_key = self.curve.scalar_multiply(self._private_key, self.G)

    def generate_shared_secret(self, other_public_key: Point) -> int:
        """
        Karşı tarafın Public Key'ini (Q_other) kullanarak ortak sırrı hesaplar.
        S_point = d * Q_other
        Shared Secret = S_point.x (Sadece x koordinatı kullanılır)
        """
        if other_public_key is None:
            raise ValueError("Gecersiz Public Key (Sonsuzdaki Nokta)!")

        # S = d * Q_other
        shared_point = self.curve.scalar_multiply(self._private_key, other_public_key)

        if shared_point is None:
            raise ValueError("Ortak sır Sonsuzdaki Nokta çıktı! (Kritik Hata)")

        # ECDH standartlarında genellikle sonucun x koordinatı ortak sır olarak alınır.
        return shared_point[0]