from pydantic import BaseModel


class Sets(BaseModel):
    reps: int
    weight: float
