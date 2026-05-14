from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/system")
def system():
    return{
        "cpu":psutil.cpu_percent(),
        "memory":psutil.virtual_memory().percent
    }