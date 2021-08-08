from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.models.request.workouts import Workout
from src.models.crud.workouts import UpdateWorkout
from src.middleware.auth import get_current_user
from src.database import get_db
from src.database import crud

router = APIRouter()


@router.post('/')
async def create_workout(workout: Workout, db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        crud.update_workout(
            db, user, {"active": False, "ended": datetime.now()})

        new_workout = crud.create_workout(db, workout, user)
        exercise_templates = crud.get_exercise_templates(
            db, workout.workoutTemplateId)

        exercise_template_ids = [
            exerciseTemplate.id for exerciseTemplate in exercise_templates]
        newExercises = crud.create_multiple_exercises(
            db, exercise_template_ids,  new_workout.id)

        return JSONResponse(content=jsonable_encoder(new_workout))
    except Exception as e:
        raise(e)


@router.get('/')
async def get_workouts(ids: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    id_array = ids.split(',')
    for id in id_array:
        print(id)
    return 'get workouts'


@router.get('/active')
async def get_active_workout(db: Session = Depends(get_db), user=Depends(get_current_user)):
    active_workout = crud.get_active_workout(db, user)
    # TODO: seperate this into its own endpoint
    exercises = crud.get_exercises(db, active_workout.id)
    # print(active_workout.dict())
    # active_workout["exercises"] = active_workout
    return JSONResponse(content=jsonable_encoder({
        "activeWorkout": active_workout,
        "exercises": exercises
    }))


@ router.get('/{workoutId}')
async def get_workouts(workoutId: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    pass


@ router.put('/')
async def update_workout(id: str, workout: Workout, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'get workout'


@ router.delete('/')
async def delete_workout(id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'delete workout'
