from typing import Optional
from pydantic import BaseModel

class ExerciseTemplate(BaseModel):
    name: str
    sets: int

class EditExerciseTemplate(BaseModel): 
    name: Optional[str]
    sets: Optional[int]


class CreateExerciseTemplate(ExerciseTemplate):
    workoutTemplateId: int


class WorkoutTemplate(BaseModel):
    name: str
    exerciseTemplates: list[ExerciseTemplate]


class EditWorkoutTemplate(BaseModel):
    name: Optional[str] 
    exerciseTemplates: Optional[list[ExerciseTemplate]]