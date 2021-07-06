from pydantic import BaseModel


class WorkoutBase(BaseModel):
    name: str
