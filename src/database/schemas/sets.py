from sqlalchemy import Column, ForeignKey, Integer, String, Float
from ..database import Base

class Set(Base):
    __tablename__ = "sets"
    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Float)
    reps = Column(Integer)

    exercise_id = Column(Integer, ForeignKey("exercise.id"))