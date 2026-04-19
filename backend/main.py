from fastapi import FastAPI
import random

app = FastAPI(
    title="Spin Wheel API",
    description="backend for spin wheel game",
    version="1.0"
)

options: list[str] = ["100", "200", "Try Again", "500", "Jackpot"]


@app.get("/options")
def get_options():
    return {
        "options": options
    }

# Sample wheel options

@app.get("/")
def home():
    return {"message": "Spin Wheel API Running 🚀"}

@app.get("/spin", summary="Spin the wheel and get a random result")
def spin_wheel() -> dict:
    result = random.choice(options)
    return {
        "success" : True,
        "result": result,
        "message": "Spin successful"
    }