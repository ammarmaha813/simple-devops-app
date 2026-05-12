from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "DevOps Agent App Running",
        "hostname": socket.gethostname(),
        "time": str(datetime.now())
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }