# Diffie-Hellman vs. ECDHE: Uygulama, Performans Analizi ve MitM Zafiyet Simülasyonu

---

## 📖 Proje Özeti

Bu proje, güvenli anahtar değişimi protokolleri olan **Klasik Diffie-Hellman (DH)** ve **Elliptic Curve Diffie-Hellman (ECDHE)** algoritmalarını derinlemesine incelemek amacıyla geliştirilmiştir. Proje, hazır kriptografi kütüphanelerini (OpenSSL, PyCryptodome vb.) "kara kutu" olarak kullanmak yerine, matematiksel temelleri (Modular Arithmetic, Elliptic Curve Group Laws) **sıfırdan (from scratch)** implemente etmiştir.

Proje metodolojisi **"Build, Measure, Break"** (İnşa Et, Ölç, Kır) felsefesine dayanmaktadır.

---

## 🛠 Mimari ve Metodoloji

Proje üç ana modülden oluşmaktadır:

### 1. Build (Kripto Motoru - `crypto_engine/`)
Hazır kütüphaneler kullanılmadan geliştirilen matematiksel çekirdektir.
*   **Klasik DH:** Python'ın optimize edilmiş `pow(base, exp, mod)` fonksiyonu üzerine kurulu protokol yapısı.
*   **ECDH:** Weierstrass formundaki eğriler ($y^2 = x^3 + ax + b$) üzerinde **Double-and-Add** algoritması ile nokta çarpımı ve toplama işlemleri.
*   **Protokoller:** Hem *Static* (sabit anahtar) hem de *Ephemeral* (her oturumda yeni anahtar - Forward Secrecy) modlarını destekleyen sınıf yapıları.

### 2. Measure (Performans Testleri - `benchmark_suite/`)
İki algoritmanın hesaplama maliyetlerini ve ağ yüklerini karşılaştırır.
*   **Test Ortamı:** Sonuçların tutarlılığı için **Docker** konteynerleri üzerinde çalışır.
*   **Senaryolar:**
    *   **DH-2048 vs ECDH-256:** (Yaklaşık 112-bit güvenlik seviyesi denkliği)
    *   **DH-3072:** Anahtar boyutu arttığında klasik DH'in performans düşüşünü (kübik karmaşıklık) gösterir.
*   **Çıktı:** Konsolda detaylı istatistikler (Ops/Sec) ve HTML formatında grafik raporu.

### 3. Break (Saldırı Laboratuvarı - `attack_visualizer/`)
Teorik zafiyetlerin pratikte nasıl sömürüldüğünü gösteren interaktif bir Web GUI (Flask + SocketIO).
*   **Small Subgroup Confinement Attack:** Araya giren saldırganın (Mallory), sunucuya $p-1$ değerini enjekte ederek ortak sırrı $\{1, -1\}$ alt grubuna hapsetmesi.
*   **Forward Secrecy (İleriye Dönük Gizlilik):** Statik anahtar ifşa olduğunda geçmiş mesajların çözülebildiğini, Ephemeral anahtarlarda ise çözülemediğini gösteren zaman çizelgesi simülasyonu.

---

## 📂 Dizin Yapısı

```text
.
├── crypto_engine/          # Kriptografik matematik çekirdeği (Build)
│   ├── elliptic_curve.py   # EC nokta toplama ve skaler çarpım
│   ├── modular_arithmetic.py # Modüler aritmetik işlemler
│   └── protocols.py        # DH ve ECDH protokol sınıfları
├── benchmark_suite/        # Performans testleri (Measure)
│   ├── benchmark.py        # Test senaryoları ve ölçüm mantığı
│   └── standard_params.py  # RFC 3526 ve NIST parametreleri
├── attack_visualizer/      # Saldırı simülasyon arayüzü (Break)
│   ├── app.py              # Flask backend ve WebSocket sunucusu
│   └── templates/          # HTML/JS arayüz dosyaları
├── Dockerfile              # Benchmark izolasyonu için Docker imajı
├── Makefile                # Kolay çalıştırma komutları
└── requirements.txt        # Web arayüzü bağımlılıkları
```

---

## 🚀 Kurulum ve Çalıştırma

Projeyi çalıştırmak için sisteminizde **Python 3.9+** ve (Benchmark için) **Docker** yüklü olmalıdır.

### Adım 1: Performans Testlerini Çalıştırma (Benchmark)

Benchmark testi, algoritmaların işlemci süresini ve ağ yükünü (Payload Size) ölçer. Docker kullanılarak izole bir ortamda çalıştırılır.

1.  **Docker İmajını Oluşturun:**
    ```bash
    make build
    ```

2.  **Testi Başlatın:**
    *   *Senaryo A (Yüksek Performanslı Sunucu):*
        ```bash
        make benchmark-server
        ```
    *   *Senaryo B (IoT Cihazı Simülasyonu - 0.5 CPU, 128MB RAM):*
        ```bash
        make benchmark-iot
        ```

3.  **Sonuçları Görüntüleyin:**
    Test tamamlandığında konsolda özet tablo görünecek ve ana dizinde `crypto_benchmark_report.html` dosyası oluşturulacaktır. Bu dosyayı tarayıcınızda açarak grafikleri inceleyebilirsiniz.

---

### Adım 2: Saldırı Laboratuvarını Çalıştırma (Attack Lab)

Bu modül, tarayıcı üzerinden çalışan interaktif bir simülasyondur.

1.  **Gerekli Paketleri Yükleyin:**
    ```bash
    pip install -r attack_visualizer/requirements.txt
    ```

2.  **Sunucuyu Başlatın:**
    ```bash
    python attack_visualizer/app.py
    ```

3.  **Arayüze Erişin:**
    Tarayıcınızda `http://localhost:5001` adresine gidin.

#### Laboratuvar Kullanım Senaryoları:
*   **Senaryo 1 (Forward Secrecy):** "Statik Oturum" ile birkaç kez mesajlaşın. Ardından "Anahtarı Sızdır" butonuna basın. Geçmiş kilitlerin hepsinin kırıldığını (kırmızı) göreceksiniz. "Ephemeral" modda ise geçmişin güvende kaldığını gözlemleyin.
*   **Senaryo 2 (MitM Saldırısı):** "Manuel Müdahale Modu"nu açın. Yeni bir oturum başlatın. Paket Mallory'de durduğunda "Alt Grup Saldırısı (P-1)" seçeneğini seçin. Şifreli mesajların saldırgan tarafından anında çözüldüğünü loglarda göreceksiniz.

---

## 📊 Beklenen Sonuçlar ve Analiz

1.  **DH-3072 Yavaşlığı:** Anahtar boyutu 2048'den 3072'ye çıktığında (%50 artış), işlem süresinin kübik karmaşıklık ($O(k^3)$) nedeniyle yaklaşık 6-7 kat yavaşladığını göreceksiniz.
2.  **ECDH Verimliliği:** ECDH-256, DH-3072 ile eşdeğer güvenlik (128-bit) sağlamasına rağmen, anahtar boyutu (Payload) ~6 kat daha küçüktür (384 Byte vs 64 Byte). Bu durum, ECDH'yi bant genişliği kısıtlı IoT ağları için ideal kılar.
3.  **Zafiyet Analizi:** Simülasyon, *public key validation* (anahtar doğrulama) yapılmayan DH uygulamalarının ne kadar kırılgan olduğunu kanıtlamaktadır.

---

## 👨‍💻 Yazar ve Lisans
**Geliştirici:** Amir Ahmed Salih (2500007643)