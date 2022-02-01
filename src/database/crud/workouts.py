import datetime as dt

from sqlalchemy.orm import Session, load_only
from sqlalchemy.orm.session import make_transient
from sqlalchemy.orm.exc import NoResultFound

from src.models.crud import workouts
from src.database import schemas, engine


def create_workout(db: Session, workout: workouts.Workout, user):
    new_workout = schemas.Workout(
        started=dt.datetime.utcnow(),
        active=True,
        user_id=user.id,
        workout_template_id=workout.workoutTemplateId,
    )
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    make_transient(new_workout)
    return new_workout

def get_workout(db: Session, user, workout_id):
    workout = db.query(schemas.WorkoutTemplate, schemas.Workout) \
        .filter(user.id == schemas.WorkoutTemplate.user_id) \
        .filter(schemas.WorkoutTemplate.id == schemas.Workout.workout_template_id) \
        .first()
    return workout.Workout

def get_workouts(user_id: int, **kwargs):
    """ get workouts of the user

    Args:
        db (Session): [description]
        user ([type]): [description]

    Returns:
        [type]: [description]
    """
    with Session(engine) as db:
        workouts = db.query(schemas.Workout).filter(schemas.Workout.user_id == user_id)

        before = kwargs.get('before', None)
        if before:
            workouts = workouts.filter(schemas.Workout.started < before)

        after = kwargs.get('after', None)
        if after:
            workouts = workouts.filter(after < schemas.Workout.started)

        active = kwargs.get('active', None)
        if active:
            workouts = workouts.filter(schemas.Workout.active == True)

        workouts = workouts.order_by(schemas.Workout.started.desc())
        
        return workouts.all()

def get_active_workout(db: Session, user):
    active_workout = db.query(schemas.WorkoutTemplate, schemas.Workout) \
        .filter(user.id == schemas.WorkoutTemplate.user_id) \
        .filter(schemas.WorkoutTemplate.id == schemas.Workout.workout_template_id) \
        .filter(schemas.Workout.active == True).first()
    if active_workout is None:
        raise NoResultFound
    return active_workout.Workout


def update_workout(db: Session, user, update_workout: dict):
    db.query(schemas.Workout).filter(user.id == schemas.WorkoutTemplate.user_id) \
        .filter(schemas.WorkoutTemplate.id == schemas.Workout.workout_template_id) \
        .filter(schemas.Workout.active == True) \
        .update(update_workout, synchronize_session=False)
    db.commit()


def delete_workout(db: Session):
    pass
