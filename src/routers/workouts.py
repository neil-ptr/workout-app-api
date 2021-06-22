from fastapi import APIRouter
from src.models.request import workouts
from src.models.request import workouts

router = APIRouter()


@router.get('/workouts')
async def get_workouts():
    return 'get workouts'


@router.post('/workouts')
async def post_workouts():
    return 'post workouts'


@router.get('/workouts')
async def get_workouts():
    return 'get workouts'
