.PHONY: build benchmark-iot benchmark-server

build:
	@echo "Building Crypto Workbench..."
	docker build -t crypto-bench .

# Runs benchmark inside limited container, pipes JSON to local report generator
benchmark-iot:
	@echo "Running Simulation: IoT / Ad-Hoc Network Node (Low CPU)..."
	docker run --rm --cpus="0.5" --memory="128m" crypto-bench python -m benchmark_suite.benchmark | python3 benchmark_suite/report_generator.py
	@echo "Opening Report..."
	# Linux/Mac için open/xdg-open, Windows için start kullanılabilir
	# open crypto_benchmark_report.html

benchmark-server:
	@echo "Running Simulation: High Performance Server..."
	docker run --rm --cpus="2.0" --memory="1g" crypto-bench python -m benchmark_suite.benchmark | python3 benchmark_suite/report_generator.py