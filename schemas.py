from pydantic import BaseModel
from datetime import datetime

# -------- USER --------
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str
# -------- CASE --------
class CaseCreate(BaseModel):
    title: str
    description: str
    location: str
    crime_type: str
    severity: str
    date_reported: datetime

class CaseResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    crime_type: str
    severity: str
    date_reported: datetime
    user_id: int
    created_at: datetime
    class Config:
        from_attributes = True

