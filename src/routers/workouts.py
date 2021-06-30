from fastapi import APIRouter

from src.models.request import workouts

router = APIRouter()


@router.get('/')
async def get_workouts():
    return 'get workouts'


@router.post('/')
async def post_workouts():
    return 'post workouts'


@router.get('/')
async def get_workouts():
    return 'get workouts'
