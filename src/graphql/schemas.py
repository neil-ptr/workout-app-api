import strawberry
from typing import List, Optional

from src.graphql.resolvers import get_exercise_templates, get_exercises, get_sets, get_exercise_template, get_workout_template

@strawberry.type
class ExerciseTemplate:
    id: int
    name: str
    reps: int
    sets: int

@strawberry.type
class WorkoutTemplate:
    id: int
    name: str
    exerciseTemplates: List['ExerciseTemplate'] = strawberry.field(resolver=get_exercise_templates)

@strawberry.type
class Workout:
    id: int
    started: str
    ended: str
    active: bool
    exercises: List['Exercise'] = strawberry.field(resolver=get_exercises)
    workoutTemplate: 'WorkoutTemplate' = strawberry.field(resolver=get_workout_template)

@strawberry.type
class Exercise:
    id: int
    exerciseTemplate: ExerciseTemplate = strawberry.field(resolver=get_exercise_template)
    sets: List['Set'] = strawberry.field(resolver=get_sets)

@strawberry.type
class Set:
    id: int
    weight: float
    reps: int

@strawberry.type
class User:
    id: int
    email: str
    firstname: str
    workouts: Optional[List[Workout]] = None
    workoutTemplates: Optional[List[WorkoutTemplate]] = None

@strawberry.type
class Tokens:
    refreshToken: str
    accessToken: str

@strawberry.type
class AuthSuccess:
    tokens: Tokens

@strawberry.type
class AuthError:
    message: str

AuthResult = strawberry.union("AuthResult", (AuthSuccess, AuthError))
