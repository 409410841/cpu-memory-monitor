from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
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
        "cpu": random.randint(0, 100),
        "memory": random.randint(0,100),
        "disk": random.randint(0,100),
        "network": random.randint(0,100)
    }