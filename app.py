from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Example metric
REQUESTS = Counter("app_requests_total", "Total HTTP requests")

@app.route("/")
def hello():
    REQUESTS.inc()
    return "Hello, World!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Add these for Kubernetes probes
@app.route("/healthz")
def healthz():
    return "ok", 200

@app.route("/ready")
def ready():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
