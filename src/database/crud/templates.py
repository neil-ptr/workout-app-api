from sqlalchemy.orm import Session

from src.database.models import templates

def create_workout_template(db: Session, workoutTemplate: templates.WorkoutTemplate):
    pass

def get_workout_template(db: Session):
    pass

def create_exercise_template(db: Session):
    pass

def get_exercise_template(db: Session):
    pass