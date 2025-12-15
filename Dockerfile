# Base image: Python 3.9 (Slim version for lighter footprint)
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Kodları konteynera kopyala
COPY crypto_engine /app/crypto_engine
COPY benchmark_suite /app/benchmark_suite
# (İleride attack_lab de eklenecek)

# Bağımlılık yok (No pip install needed for pure math implementation!)
# Ancak ileride grafik çizmek gerekirse matplotlib eklenebilir.

# Benchmark scriptini çalıştır
CMD ["python", "-m", "benchmark_suite.benchmark"]