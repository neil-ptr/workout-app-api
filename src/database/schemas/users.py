from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .accounts import Account
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String)
    hashed_password = Column(String)

    workouts = relationship("Workout", back_populates="user")
    workout_templates = relationship("WorkoutTemplate", back_populates="user")
    account = relationship("Account", back_populates="user", uselist=False)
