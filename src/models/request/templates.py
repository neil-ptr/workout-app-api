from pydantic import BaseModel

class ExerciseTemplate(BaseModel):
    name: str
    sets: int


class CreateExerciseTemplate(ExerciseTemplate):
    workoutTemplateId: int


class WorkoutTemplate(BaseModel):
    name: str
    exerciseTemplates: list[ExerciseTemplate]
