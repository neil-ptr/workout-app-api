from fastapi import APIRouter

from src.models.request import exercises

router = APIRouter()


@router.get('/')
async def get_exercises():
    return 'get exercises'


@router.post('/')
async def create_exercises():
    return 'post exercises'


@router.put('/')
async def update_exercise():
    return 'get exercise'

@router.delete('/')
async def delete_exercise():
    return 'delete exercise'
