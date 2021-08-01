from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.models.request.workouts import Workout
from src.middleware.auth import get_current_user
from src.database import get_db
from src.database import crud

router = APIRouter()


@router.post('/')
async def create_workout(workout: Workout, db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        newWorkout = crud.create_workout(db, workout, user)

        exerciseTemplates = crud.get_exercise_templates(
            db, workout.workoutTemplateId)

        exerciseTemplateIds = [
            exerciseTemplate.id for exerciseTemplate in exerciseTemplates]
        print(exerciseTemplateIds)
        newExercises = crud.create_multiple_exercises(db, exerciseTemplateIds)

        return JSONResponse(content=jsonable_encoder({'workout': newWorkout, 'exercises': newExercises}))
    except Exception as e:
        raise(e)


@router.get('/')
async def get_workouts(ids: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    id_array = ids.split(',')
    for id in id_array:
        print(id)
    return 'get workouts'


@router.put('/')
async def update_workout(id: str, workout: Workout, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'get workout'


@router.delete('/')
async def delete_workout(id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'delete workout'
