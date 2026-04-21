from pydantic import BaseModel
from fastapi import FastAPI
import random

app = FastAPI(
    title="Spin Wheel API",
    description="backend for spin wheel game",
    version="1.0"
)

wheel_data = [
    {"label": "100", "weight": 1},
    {"label": "200", "weight": 1},
    {"label": "Try Again", "weight": 2},
    {"label": "500", "weight": 0.5},
    {"label": "Jackpot", "weight": 0.1}

]

class WheelItem(BaseModel):
    label : str
    weight: float

@app.get("/options")
def get_options():
    return {
        "options": wheel_data
    }

# Sample wheel options

@app.get("/")
def home():
    return {"message": "Spin Wheel API Running 🚀"}

@app.get("/spin", summary="Spin the wheel and get a random result")
def spin_wheel() -> dict:
    labels = [item["label"] for item in wheel_data]
    weights = [item["weight"] for item in wheel_data]

    result = random.choices(labels, weights= weights, k=1 )[0]

    return{
        "success": True,
        "result": result,
        "message": "Spin successful"
    }

@app.post("/set-options")
def set_options(new_options: list[WheelItem]):
    global wheel_data
    wheel_data = [item.dict() for item in new_options]

    return {
        "success": True,
        "message": "Wheel options updated",
        "data": wheel_data
    }
