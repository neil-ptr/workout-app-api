from fastapi import APIRouter, Depends
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.database.utils import object_as_dict
from src.models.request.workouts import Workout
from src.middleware.auth import get_current_user
from src.database import get_db
from src.database import crud

router = APIRouter()


@router.post('/')
async def create_workout(workout: Workout, db: Session = Depends(get_db), user=Depends(get_current_user)):
    """ turn all other workouts to inactive and start new workout
    """
    # ensure that the new workout is the only active workout
    crud.update_workout(db, user, {'active': False})
    new_workout = crud.create_workout(db, workout, user)
    exercise_templates = crud.get_exercise_templates(
        db, workout.workoutTemplateId)

    exercise_template_ids = [
        exerciseTemplate.id for exerciseTemplate in exercise_templates]
    crud.create_multiple_exercises(
        db, exercise_template_ids,  new_workout.id)

    exercises = crud.get_exercises(db, new_workout.id)

    # build workout object to return
    workout_obj = {
        'id': new_workout.id, 
        'active': new_workout.active,
        'workout_template_id': new_workout.workout_template_id, 
        'ended': new_workout.ended, 
        'started': new_workout.started, 
        'user_id': new_workout.user_id,
        'exercises': exercises
    }

    return JSONResponse(content=jsonable_encoder(workout_obj))


@router.get('/active')
async def get_active_workout(db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        active_workout = crud.get_active_workout(db, user)
        exercise_data = crud.get_exercises(db, active_workout.id)

        exercises = []

        for exercise in exercise_data:
            exercises.append({
                'exercise': object_as_dict(exercise.Exercise),
                'exerciseTemplate': object_as_dict(exercise.ExerciseTemplate),
                'sets': [object_as_dict(set) for set in crud.get_sets(db, exercise.Exercise.id)]
            })

        return JSONResponse(content=jsonable_encoder({
            "activeWorkout": active_workout,
            "workoutData": exercises
        }))

    except NoResultFound:
        return JSONResponse(content=jsonable_encoder({
            "activeWorkout": None,
            "workoutData": []
        }))

@router.get('/endActiveWorkout')
async def end_active_workout(db: Session = Depends(get_db), user=Depends(get_current_user)):
    crud.update_workout(db, user, {'active': False})