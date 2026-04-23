from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

models.base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Spin Wheel API",
    description="backend for spin wheel game",
    version="1.0"
)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

wheel_data = [
    {"label": "100", "weight": 1},
    {"label": "200", "weight": 1},
    {"label": "Try Again", "weight": 2},
    {"label": "500", "weight": 0.5},
    {"label": "Jackpot", "weight": 0.1}

]

class WheelItem(BaseModel):
    label : str = Field(..., min_lenght=1)
    weight: float = Field(..., gt=0)

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
