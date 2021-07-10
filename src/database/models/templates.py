from pydantic import BaseModel


class ExerciseTemplate(BaseModel):
    name: str


class WorkoutTemplate(BaseModel):
    name: str
    exerciseTemplates: list[ExerciseTemplate]
