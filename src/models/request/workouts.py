from pydantic import BaseModel

from .exercises import Exercise


class Workout(BaseModel):
    name: str
    exercises: list[Exercise]