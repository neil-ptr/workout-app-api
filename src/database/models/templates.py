from pydantic import BaseModel


class WorkoutTemplate(BaseModel):
    name: str


class ExerciseTemplate(BaseModel):
    workoutTemplateId: int
    name: str