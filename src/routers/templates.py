from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.middleware.auth import get_current_user
from src.models.request.templates import WorkoutTemplate, ExerciseTemplate, CreateExerciseTemplate
from src.database.crud import templates as crud

router = APIRouter()


@router.post('/workouts')
async def create_workouts_template(workoutTemplate: WorkoutTemplate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    newWorkoutTemplate = crud.create_workout_template(db, workoutTemplate, user.id)
    return  newWorkoutTemplate


@router.get('/workouts')
async def get_workouts_template(db: Session = Depends(get_db), user = Depends(get_current_user)):
    workoutTemplates = crud.get_workout_templates(db, user.id)
    return workoutTemplates


@router.put('/workouts')
async def update_workouts_template(workoutTemplate: WorkoutTemplate, user = Depends(get_current_user)):
    # TODO
    return 'edit workouts'


@router.delete('/workouts')
async def delete_workouts_template(workoutTemplate: WorkoutTemplate, user = Depends(get_current_user)):
    # TODO
    return 'delete workout'


@router.post('/exercises')
async def create_exercise_template(createExerciseTemplate: CreateExerciseTemplate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    exerciseTemplate = ExerciseTemplate(name=createExerciseTemplate.name)
    newExerciseTemplate = crud.create_exercise_template(db, exerciseTemplate, createExerciseTemplate.workoutTemplateId)
    return newExerciseTemplate


@router.get('/exercises')
async def get_exercise_template(workoutTemplateId: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    exerciseTemplates = crud.get_exercise_templates(db, workoutTemplateId)
    return exerciseTemplates


@router.put('/exercises')
async def update_exercise_template(exerciseTemplate: ExerciseTemplate, user = Depends(get_current_user)):
    # TODO
    return 'get exercise'


@router.delete('/exercises')
async def delete_exercise_template(exerciseTemplate: ExerciseTemplate, user = Depends(get_current_user)):
    # TODO
    return 'delete exercise'
