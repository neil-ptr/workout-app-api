from sqlalchemy.orm import Session

from src.models.crud.templates import WorkoutTemplate, ExerciseTemplate
from src.database import schemas

def create_workout_template(db: Session, workoutTemplate: WorkoutTemplate, user_id: int):
    newWorkoutTemplate = schemas.WorkoutTemplate(name=workoutTemplate.name, user_id=user_id)
    db.add(newWorkoutTemplate)
    db.flush()
    exerciseTemplates = []

    for exerciseTemplate in workoutTemplate.exerciseTemplates:
        exerciseTemplates.append(schemas.ExerciseTemplate(name=exerciseTemplate.name, workout_template_id=newWorkoutTemplate.id, sets=exerciseTemplate.sets))
    db.bulk_save_objects(exerciseTemplates)

    db.commit()
    db.refresh(newWorkoutTemplate)
    return newWorkoutTemplate

def get_workout_templates(db: Session, user_id: int):
    workoutTemplates = db.query(schemas.WorkoutTemplate).filter(schemas.WorkoutTemplate.user_id == user_id).all()
    return workoutTemplates

def update_workout_template(db: Session):
    pass

def delete_workout_template(db: Session):
    pass

def create_exercise_template(db: Session, exerciseTemplate: ExerciseTemplate, workoutTemplateId: int):
    newExerciseTemplate = schemas.ExerciseTemplate(name=exerciseTemplate.name, workout_template_id=workoutTemplateId)
    db.add(newExerciseTemplate)
    db.commit()
    db.refresh(newExerciseTemplate)
    return newExerciseTemplate

def get_exercise_templates(db: Session, workout_template_id: int):
    queryConstraint = schemas.ExerciseTemplate.workout_template_id == workout_template_id
    exerciseTemplates = db.query(schemas.ExerciseTemplate).all()
    return exerciseTemplates

def update_exercise_template(db: Session):
    pass

def delete_exercise_template(db: Session):
    pass