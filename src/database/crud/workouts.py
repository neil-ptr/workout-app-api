from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.models.crud import workouts
from src.database import schemas

def create_workout(db: Session, workout: workouts.Workout, user):
    newWorkout = schemas.Workout(
        started=workout.started,
        ended=workout.ended,
        active=True,
        user_id=user.id,
        workout_template_id=workout.workout_template_id,
    )
    return JSONResponse(content=jsonable_encoder(newWorkout))

def get_workouts(db: Session, workout_id_array: list[str]):
    pass

def update_workout(db: Session):
    pass

def delete_workout(db: Session):
    pass