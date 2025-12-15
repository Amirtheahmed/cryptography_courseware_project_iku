import json
import sys
import datetime

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cryptographic Benchmark: DH vs ECDH</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; padding: 20px; background: #f4f4f9; }
        .container { max-width: 1000px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
        .meta { color: #666; font-size: 0.9em; margin-bottom: 20px; }
        .chart-box { margin-bottom: 40px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #007bff; color: white; }
    </style>
</head>
<body>
<div class="container">
    <h1>Diffie-Hellman vs. ECDHE Performance Analysis</h1>
    <div class="meta">Generated on: <span id="date"></span> | Environment: Docker Container</div>

    <div class="chart-box">
        <h3>Execution Time Comparison (Lower is Better)</h3>
        <canvas id="timeChart"></canvas>
    </div>

    <div class="chart-box">
        <h3>Network Payload Efficiency (Lower is Better)</h3>
        <canvas id="sizeChart"></canvas>
    </div>

    <h3>Detailed Data</h3>
    <table id="dataTable">
        <tr><th>Algorithm</th><th>KeyGen (s)</th><th>Handshake (s)</th><th>Payload (Bytes)</th></tr>
    </table>
</div>

<script>
    const data = DATA_PLACEHOLDER;
    document.getElementById('date').innerText = new Date().toLocaleString();

    // Populate Table
    const table = document.getElementById('dataTable');
    data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${row.algorithm}</td><td>${row.keygen_avg_sec.toFixed(4)}</td><td>${row.handshake_avg_sec.toFixed(4)}</td><td>${row.payload_bytes}</td>`;
        table.appendChild(tr);
    });

    // Chart 1: Time
    new Chart(document.getElementById('timeChart'), {
        type: 'bar',
        data: {
            labels: data.map(d => d.algorithm),
            datasets: [
                { label: 'Key Generation (s)', data: data.map(d => d.keygen_avg_sec), backgroundColor: '#36a2eb' },
                { label: 'Handshake (s)', data: data.map(d => d.handshake_avg_sec), backgroundColor: '#ff6384' }
            ]
        },
        options: { scales: { y: { beginAtZero: true, title: {display: true, text: 'Seconds'} } } }
    });

    // Chart 2: Size
    new Chart(document.getElementById('sizeChart'), {
        type: 'bar',
        data: {
            labels: data.map(d => d.algorithm),
            datasets: [{ label: 'Public Key Size (Bytes)', data: data.map(d => d.payload_bytes), backgroundColor: '#4bc0c0' }]
        },
        options: { indexAxis: 'y' }
    });
</script>
</body>
</html>
"""


def generate_report(json_data):
    data = json.loads(json_data)
    html_content = HTML_TEMPLATE.replace("DATA_PLACEHOLDER", json.dumps(data))

    filename = "crypto_benchmark_report.html"
    with open(filename, "w") as f:
        f.write(html_content)
    print(f"Report generated: {filename}")


if __name__ == "__main__":
    # Read JSON from stdin
    input_data = sys.stdin.read()
    generate_report(input_data)