from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from ..database import Base


class Exercise_Template(Base):
    __tablename__ = "exercise_templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128))

    workout_template_id = Column(Integer, ForeignKey("workout_templates.id"))
    workout_template = relationship("WorkoutTemplate", back_populates="exercise_templates")
    exercise = relationship("Exercise", back_populates="exercise_template")


class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, index=True)
    duration = Column(Integer)
    active = Column(Boolean, default=True)
    # duration = Integer TODO

    exercise_template_id = Column(Integer, ForeignKey("exercise_template.id"))
    exercise_template = relationship("ExerciseTemplate", back_populates="exercises")
    