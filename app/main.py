from fastapi import FastAPI
from datetime import datetime
import socket
import os

app = FastAPI()

PORT = int(os.getenv("PORT", 8000))

@app.get("/")
def home():
    return {
        "message": "Simple API running",
        "hostname": socket.gethostname(),
        "time": str(datetime.now()),
        "port": PORT
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/users")
def users():
    return [
        {"id": 1, "name": "Maha"},
        {"id": 2, "name": "DevOps User"}
    ]