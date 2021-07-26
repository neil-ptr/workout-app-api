from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models.request.workouts import Workout
from src.database import get_db
from src.database.crud import workouts as crud

router = APIRouter()

@router.post('/')
async def create_workout(workout: Workout, db: Session = Depends(get_db)):
    crud.create_workout(db, workout)
    return 'create workout'


@router.get('/')
async def get_workouts(ids: str, db: Session = Depends(get_db)):
    id_array = ids.split(',')
    for id in id_array:
        print(id)
    return 'get workouts'


@router.put('/')
async def update_workout(id: str, workout: Workout, db: Session = Depends(get_db)):
    return 'get workout'


@router.delete('/')
async def delete_workout(id: str):
    return 'delete workout'
