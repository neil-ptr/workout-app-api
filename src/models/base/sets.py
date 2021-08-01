from pydantic import BaseModel


class SetsBase(BaseModel):
    reps: int
    weight: float
