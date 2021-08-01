from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.middleware.auth import get_current_user
from src.database import get_db
from src.models.request import exercises
from src.database import crud

router = APIRouter()


@router.get('/')
async def get_exercises(db: Session = Depends(get_db), user=Depends(get_current_user)):
    # crud.get_exercises(db,)
    pass


@router.post('/')
async def create_exercises(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'post exercises'


@router.put('/')
async def update_exercise(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'get exercise'


@router.delete('/')
async def delete_exercise(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'delete exercise'
