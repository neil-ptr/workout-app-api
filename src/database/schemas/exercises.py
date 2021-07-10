from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from ..database import Base


class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, index=True)
    duration = Column(Integer)
    active = Column(Boolean, default=True)
    # duration = Integer TODO

    exercise_template_id = Column(Integer, ForeignKey("exercise_templates.id"))
    exercise_template = relationship("ExerciseTemplate", back_populates="exercises")
    