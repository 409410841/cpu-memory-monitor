from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/system")
def get_metrics():

    cpu = psutil.cpu_percent()

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/").percent

    network = psutil.net_io_counters().bytes_sent / 1024 / 1024

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "network": round(network, 2)
    }