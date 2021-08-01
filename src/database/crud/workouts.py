from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.models.crud import workouts
from src.database import schemas

def create_workout(db: Session, workout: workouts.Workout, user):
    # TODO: turn all other workouts to unactive
    newWorkout = schemas.Workout(
        started=workout.started,
        active=True,
        user_id=user.id,
        workout_template_id=workout.workoutTemplateId,
    )
    db.add(newWorkout)
    db.commit()
    db.refresh(newWorkout)
    return newWorkout

def get_workouts(db: Session, workout_id_array: list[str]):
    pass

def update_workout(db: Session):
    pass

def delete_workout(db: Session):
    pass