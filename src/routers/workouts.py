from fastapi import APIRouter

from src.models.request.workouts import Workout

router = APIRouter()

@router.post('/')
async def create_workout(workout: Workout):
    return 'create workout'


@router.get('/')
async def get_workouts(ids: str):
    id_array = ids.split(',')
    for id in id_array:
        print(id)
    return 'get workouts'


@router.put('/')
async def update_workout(id: str, workout: Workout):
    return 'get workout'


@router.delete('/')
async def delete_workout(id: str):
    return 'delete workout'
