from sqlalchemy.orm import Session

from src.models.crud import exercises
from src.database import schemas


def create_exercise(db: Session, exercise_template_id: int, workout_id: int):
    new_exercise = schemas.Exercise(
        exercise_template_id=exercise_template_id, workout_id=workout_id)
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    return new_exercise


def create_multiple_exercises(db: Session, exercise_template_ids, workoutId):
    new_exercises = []
    for exercise_template_id in exercise_template_ids:
        new_exercises.append(schemas.Exercise(
            exercise_template_id=exercise_template_id, workout_id=workoutId))

    db.add_all(new_exercises)
    db.commit()
    return new_exercises

def get_exercise(db: Session, exercise_id: int, user_id: int): 
    """ get single exercise by id

    Args:
        db (Session): db connection
        exercise_id (int): id of the exercise to et
        user_id (int): id of the user

    Returns:
        [type]: [description]
    """
    return db.query(schemas.Exercise) \
        .filter(schemas.Exercise.id == exercise_id) \
        .first()

def get_exercises(db: Session, workout_id: int):
    """ get the exercises of a workout

    Args:
        db (Session): db connection
        workout_id (int): id of the workout to get exercises for

    Returns:
        List of exercise and exercise templates   
    """
    return db.query(schemas.Exercise, schemas.ExerciseTemplate) \
        .filter(schemas.Exercise.workout_id == workout_id) \
        .filter(schemas.ExerciseTemplate.id == schemas.Exercise.exercise_template_id) \
        .all()
