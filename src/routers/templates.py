from fastapi import APIRouter

from src.models.request.templates import WorkoutTemplate, ExerciseTemplate


router = APIRouter()


@router.get('/exercises')
async def get_exercise_template():
    return 'get exercises'


@router.post('/exercises')
async def create_exercise_template():
    return 'post exercises'


@router.put('/exercises')
async def update_exercise_template():
    return 'get exercise'


@router.delete('/exercises')
async def delete_exercise_template():
    return 'delete exercise'


@router.get('/workouts')
async def get_workouts_template(workoutTemplate: WorkoutTemplate):
    return 'get exercises'


@router.post('/workouts')
async def create_workouts_template(workoutTemplate: WorkoutTemplate):
    print(workoutTemplate)
    return 'post exercises'


@router.put('/workouts')
async def update_workouts_template(workoutTemplate: WorkoutTemplate):
    return 'get exercise'


@router.delete('/workouts')
async def delete_workouts_template(workoutTemplate: WorkoutTemplate):
    return 'delete exercise'
