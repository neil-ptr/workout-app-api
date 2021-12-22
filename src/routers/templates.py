from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.middleware.auth import get_current_user
from src.models.request.templates import WorkoutTemplate, ExerciseTemplate, CreateExerciseTemplate, EditWorkoutTemplate, EditExerciseTemplate
from src.database.crud import templates as crud

router = APIRouter()


@router.post('/workouts')
async def create_workouts_template(workoutTemplate: WorkoutTemplate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """ new workout template
    """
    newWorkoutTemplate = crud.create_workout_template(db, workoutTemplate, user.id)
    return  newWorkoutTemplate


@router.get('/workouts/{user_id}')
async def get_workouts_template(db: Session = Depends(get_db), user = Depends(get_current_user)):
    """ get workout templates of a user
    """
    workoutTemplates = crud.get_workout_templates(db, user.id)
    return workoutTemplates


@router.put('/workouts')
async def update_workouts_template(editWorkoutTemplate: EditWorkoutTemplate, user = Depends(get_current_user)):
    """ update workout template
    """
    return 'edit workouts'


@router.delete('/workouts/{id}')
async def delete_workouts_template(id: int, user = Depends(get_current_user)):
    """ delete workout template
    """
    return 'delete workout'


@router.post('/exercises')
async def create_exercise_template(createExerciseTemplate: CreateExerciseTemplate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """ create exercise template
    """
    exerciseTemplate = ExerciseTemplate(name=createExerciseTemplate.name)
    newExerciseTemplate = crud.create_exercise_template(db, exerciseTemplate, createExerciseTemplate.workoutTemplateId)
    return newExerciseTemplate


@router.get('/exercises/{workout_id}')
async def get_exercise_template(workoutTemplateId: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """ get exercise templates
    """
    exerciseTemplates = crud.get_exercise_templates(db, workoutTemplateId)
    print(exerciseTemplates)
    return exerciseTemplates


@router.put('/exercises/{exercise_template_id}')
async def update_exercise_template(editExerciseTemplate: EditExerciseTemplate, user = Depends(get_current_user)):
    """ update exercise template
    """
    return 'get exercise'


@router.delete('/exercises/{exercise_template_id}')
async def delete_exercise_template(id: int, user = Depends(get_current_user)):
    """ delete exercise template
    """
    return 'delete exercise'
