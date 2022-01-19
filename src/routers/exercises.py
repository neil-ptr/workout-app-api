from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.middleware.auth import get_current_user
from src.database import get_db
from src.models.request import exercises
from src.database import crud

router = APIRouter()

@router.post("/")
async def create_exercise(exerciseTemplateId: int, workoutId: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_exercise = crud.create_exercise(db, user, exerciseTemplateId, workoutId)

@router.get("/{exercise_id}")
async def get_exercise(exercise_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_sets = crud.get_sets(db, exercise_id)
    db_exercise = crud.get_exercise(db, exercise_id, user.id)
    return {
        "sets": db_sets,
        "exercise": db_exercise
    }
