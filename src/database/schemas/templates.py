from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Exercise_Template(Base):
    __tablename__ = "exercise_templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128))

    workout_template_id = Column(Integer, ForeignKey("workout_templates.id"))
    workout_template = relationship("WorkoutTemplate", back_populates="exercise_templates")
    exercise = relationship("Exercise", back_populates="exercise_template")

class WorkoutTemplate(Base):
    __tablename__ = "workout_templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="workout_templates")
    workouts = relationship("Workout", back_populates="workout_template")
    exercise_templates = relationship("ExerciseTemplate", back_populates="workout_template")
