import strawberry
from typing import List, Optional

from src.database import crud
from .schemas import User, WorkoutTemplate, Workout, Exercise


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> User:
        return crud.get_user(id)

    @strawberry.field
    def workout(self, active: Optional[bool] = False, before: Optional[str] = None, after: Optional[str] = None) -> List[Workout]:
        workouts = crud.get_workouts(6, active=active, before=before, after=after)
        return workouts

    @strawberry.field
    def workoutTemplate(self, user_id: int) -> List[WorkoutTemplate]:
        workout_template = crud.get_workout_templates(user_id)
        return workout_template

    @strawberry.field
    def exercises(self, workout_id: int) -> List[Exercise]:
        exercises = crud.get_exercises(workout_id)
        return exercises
