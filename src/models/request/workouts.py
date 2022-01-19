from pydantic import BaseModel

class Workout(BaseModel):
    workoutTemplateId: int
