from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from database import Base
from sqlalchemy.sql import func
# ----------------------
# User table
# ----------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)


# ----------------------
# Case table
# ----------------------
class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)           # Short title of crime
    description = Column(String, nullable=False)     # Full description
    location = Column(String, nullable=False)        # Crime location
    crime_type = Column(String, nullable=True)       # To be classified by AI
    severity = Column(String, nullable=True)         # e.g., Low/Medium/High
    date_reported = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
