from sqlalchemy.orm import Session
from sqlalchemy import update, and_
from sqlalchemy.orm.session import make_transient
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
    make_transient(newWorkout)
    return newWorkout


def get_workouts(db: Session, workout_id_array: list[str]):
    pass


def get_active_workout(db: Session, user):
    active_workout = db.query(schemas.WorkoutTemplate, schemas.Workout) \
        .filter(user.id == schemas.WorkoutTemplate.user_id) \
        .filter(schemas.WorkoutTemplate.id == schemas.Workout.workout_template_id) \
        .filter(schemas.Workout.active == True).first()
    return active_workout.Workout


def update_workout(db: Session, user, update_workout: dict):
    db.query(schemas.Workout).filter(user.id == schemas.WorkoutTemplate.user_id) \
        .filter(schemas.WorkoutTemplate.id == schemas.Workout.workout_template_id) \
        .filter(schemas.Workout.active == True) \
        .update(update_workout, synchronize_session=False)
    db.commit()


def delete_workout(db: Session):
    pass
