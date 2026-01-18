from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/users", tags=["Users"])


# ✅ REGISTER USER
@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        name=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "username": new_user.name,
        "email": new_user.email
    }


# ✅ LOGIN USER (FIXED)
@router.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(
        models.User.name == user.username,
        models.User.password == user.password
    ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "message": "Login successful",
        "user_id": db_user.id,
        "username": db_user.name
    }


# ✅ GET ALL USERS
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
