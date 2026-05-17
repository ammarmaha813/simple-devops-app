from fastapi import FastAPI
from datetime import datetime
import socket
import os

# Prometheus
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

PORT = int(os.getenv("PORT", 8000))

# Metrics
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)

@app.get("/")
def home():
    REQUEST_COUNT.inc()

    return {
        "message": "Simple API running",
        "hostname": socket.gethostname(),
        "time": str(datetime.now()),
        "port": PORT
    }

@app.get("/health")
def health():
    REQUEST_COUNT.inc()

    return {
        "status": "healthy"
    }

@app.get("/users")
def users():
    REQUEST_COUNT.inc()

    return [
        {"id": 1, "name": "Maha"},
        {"id": 2, "name": "DevOps User"}
    ]

# Endpoint Prometheus
@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )