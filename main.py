from fastapi import FastAPI
from user_routes import router as user_router
from case_routes import router as case_router
app = FastAPI(title="Crime Report Generator")
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from database import engine
import models
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add_user")
def add_user(name: str, role: str, password: str, db: Session = Depends(get_db)):
    new_user = User(name=name, role=role, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"User {new_user.name} added successfully", "id": new_user.id}

@app.get("/")
def home():
    return {"message": "Crime Report Generator API is running",
        "docs": "/docs",
        "users_api": "/users",
        "cases_api": "/cases"
    }

app.include_router(user_router)
app.include_router(case_router)



