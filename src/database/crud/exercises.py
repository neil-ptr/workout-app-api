from sqlalchemy.orm import Session

from src.models.crud import exercises
from src.database import schemas


def create_exercise(db: Session, exerciseTemplateId):
    newExercise = schemas.Exercise(
        exercise_template_id=exerciseTemplateId)
    db.add(newExercise)
    db.commit()
    db.refresh(newExercise)
    return newExercise


def create_multiple_exercises(db: Session, exerciseTemplateIds):
    newExercises = []
    for exerciseTemplateId in exerciseTemplateIds:
        newExercises.append(schemas.Exercise(
            exercise_template_id=exerciseTemplateId))
    db.bulk_save_objects(newExercises)
    db.commit()
    return newExercises


def get_exercises(db: Session, workout_id_array: list[str]):
    workoutTemplates = db.query(schemas.Exercise).filter(
        schemas.Exercise.id.in_(tuple(workout_id_array))).all()
    return workoutTemplates


def update_exercise(db: Session):
    pass


def delete_exercise(db: Session):
    pass
