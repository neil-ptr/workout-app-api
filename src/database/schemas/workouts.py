from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True)
    started = Column(DateTime)
    ended = Column(DateTime)
    active = Column(Boolean, default=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="workouts")
    workout_template_id = Column(Integer, ForeignKey("workout_templates.id"))
    workout_template = relationship("WorkoutTemplate", back_populates="workouts")
