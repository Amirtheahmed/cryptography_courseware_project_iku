.PHONY: build run-iot-benchmark run-server-benchmark

build:
	@echo "Docker imajı oluşturuluyor..."
	docker build -t crypto-bench .

run-iot-benchmark:
	@echo "IoT Benchmark'ı çalıştıriliyor..."
	docker run --cpus="0.5" --memory="128m" --rm crypto-bench

run-server-benchmark:
	@echo "Genel Server Benchmark'ı çalıştıriliyor..."
	docker run --rm crypto-bench --cpus="2.0" --memory="1g"