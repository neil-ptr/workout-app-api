from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.request import exercises

router = APIRouter()


@router.get('/')
async def get_exercises(db: Session = Depends(get_db)):
    return 'get exercises'


@router.post('/')
async def create_exercises(db: Session = Depends(get_db)):
    return 'post exercises'


@router.put('/')
async def update_exercise(db: Session = Depends(get_db)):
    return 'get exercise'

@router.delete('/')
async def delete_exercise(db: Session = Depends(get_db)):
    return 'delete exercise'
