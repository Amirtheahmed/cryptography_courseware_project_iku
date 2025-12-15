.PHONY: build benchmark-compare clean

build:
	@echo "Building Crypto Workbench..."
	docker build -t crypto-bench .

# Combined Benchmark: Runs both scenarios and merges results
benchmark-compare:
	@echo "\n======================================================="
	@echo "PHASE 1: Running Simulation [IoT Node / Low Spec]"
	@echo "Constraints: 0.5 CPU, 128MB RAM"
	@echo "======================================================="
	docker run --rm --cpus="0.5" --memory="128m" crypto-bench python -m benchmark_suite.benchmark > results_iot.json

	@echo "\n======================================================="
	@echo "PHASE 2: Running Simulation [Server / High Spec]"
	@echo "Constraints: 2.0 CPU, 1GB RAM"
	@echo "======================================================="
	docker run --rm --cpus="2.0" --memory="1g" crypto-bench python -m benchmark_suite.benchmark > results_server.json

	@echo "\n======================================================="
	@echo "PHASE 3: Generating Comparison Report"
	@echo "======================================================="
	python3 benchmark_suite/report_generator.py --env IoT=results_iot.json --env Server=results_server.json

	@echo "Cleaning up temporary files..."
	@rm results_iot.json results_server.json
	@echo "Done! Open 'crypto_benchmark_report.html' to see the comparison."

clean:
	rm -f *.html
	find . -type d -name "__pycache__" -exec rm -rf {} +

attack-visualizer:
	python attack_visualizer/app.py