from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .users import User
from ..database import Base

class WorkoutTemplate(Base):
    __tablename__ = "workout_templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="workout_templates")
    workouts = relationship("Workout", back_populates="workout_template")
    exercise_templates = relationship("ExerciseTemplate", back_populates="workout_template")

class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    active = Column(Boolean, default=True)
    # duration = Integer TODO

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="workouts")
    workout_template_id = Column(Integer, ForeignKey("workout_templates.id"))
    workout_templates = relationship("WorkoutTemplate", back_populates="workouts")
