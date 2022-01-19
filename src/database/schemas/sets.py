from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from ..database import Base


class Set(Base):
    __tablename__ = "sets"
    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Float, default=0)
    reps = Column(Integer, default=0)

    exercise_id = Column('exercise_id', Integer, ForeignKey("exercises.id"))
    exercise = relationship("Exercise", back_populates="sets")
