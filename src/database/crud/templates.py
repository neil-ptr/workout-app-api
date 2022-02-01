from typing import *
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from src.models.crud.templates import WorkoutTemplate, ExerciseTemplate
from src.database import schemas, engine


def create_workout_template(db: Session, workoutTemplate: WorkoutTemplate, user_id: int):
    """ save workout template

    Args:
        db (Session): database connection
        workoutTemplate (WorkoutTemplate): template
        user_id (int): id of the user

    Returns:
        (NewWorkoutTemplate): new workout template that is saved in db
    """
    newWorkoutTemplate = schemas.WorkoutTemplate(
        name=workoutTemplate.name, user_id=user_id)
    db.add(newWorkoutTemplate)
    db.flush()
    exerciseTemplates = []

    for exerciseTemplate in workoutTemplate.exerciseTemplates:
        exerciseTemplates.append(schemas.ExerciseTemplate(
            name=exerciseTemplate.name, workout_template_id=newWorkoutTemplate.id, sets=exerciseTemplate.sets, reps=exerciseTemplate.reps))
    db.bulk_save_objects(exerciseTemplates)

    db.commit()
    db.refresh(newWorkoutTemplate)
    return newWorkoutTemplate

def get_workout_template(workout_id: int):
    with Session(engine) as db:
        workoutTemplate = db.query(schemas.WorkoutTemplate).filter(
        schemas.WorkoutTemplate.id == workout_id).first()
        return workoutTemplate

def get_workout_templates(user_id: int):
    """ get all workout templates of user

    Args:
        db (Session): database connection
        user_id (int): users db id

    Returns:
        (List[WorkoutTemplate]): all workout templates of user
    """
    with Session(engine) as db:
        workoutTemplates = db.query(schemas.WorkoutTemplate).filter(
        schemas.WorkoutTemplate.user_id == user_id).all()
        return workoutTemplates


def delete_workout_template(db: Session, workout_id: int):
    """[summary]

    Args:
        db (Session): database connection
        workout_id (int): id of workout template to delete

    Raises:
        NoResultFound: Could not find workout template with given id
    """
    query_constraint = schemas.WorkoutTemplate.id == workout_id
    workout_template = db.query(schemas.WorkoutTemplate).filter(query_constraint).first()
    if workout_template is None:
        raise NoResultFound
    db.delete(workout_template)
    db.commit()


def create_exercise_template(exerciseTemplate: ExerciseTemplate, workoutTemplateId: int):
    with Session(engine) as db:
        new_exercise_template = schemas.ExerciseTemplate(
            name=exerciseTemplate.name, workout_template_id=workoutTemplateId)
        db.add(new_exercise_template)
        db.commit()
        db.refresh(new_exercise_template)
        return new_exercise_template


def get_exercise_templates(workout_template_id: int):
    with Session(engine) as db:
        query_constraint = schemas.ExerciseTemplate.workout_template_id == workout_template_id
        exercise_templates = db.query(
            schemas.ExerciseTemplate).filter(query_constraint).all()
        return exercise_templates

def get_exercise_template(exercise_template_id: int):
    with Session(engine) as db:
        query_constraint = schemas.ExerciseTemplate.id == exercise_template_id
        exercise_templates = db.query(
            schemas.ExerciseTemplate).filter(query_constraint).first()
        return exercise_templates