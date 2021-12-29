from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from starlette.responses import JSONResponse


from src.database import get_db
from src.middleware.auth import get_current_user
from src.models.request.templates import WorkoutTemplate, ExerciseTemplate, CreateExerciseTemplate, EditWorkoutTemplate, EditExerciseTemplate
from src.database.crud import templates as crud

router = APIRouter()


@router.post('/workouts')
async def create_workouts_template(workoutTemplate: WorkoutTemplate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """ create new workout template
    """
    newWorkoutTemplate = crud.create_workout_template(db, workoutTemplate, user.id)
    return  newWorkoutTemplate


@router.get('/workouts')
async def get_workouts_template(db: Session = Depends(get_db), user = Depends(get_current_user)):
    """ get workout templates of the authenticated user
    """
    workoutTemplates = crud.get_workout_templates(db, user.id)
    return workoutTemplates


@router.delete('/workouts/{id}')
async def delete_workouts_template(id: int, user = Depends(get_current_user), db: Session = Depends(get_db)):
    """ delete workout template
    """
    try:
        crud.delete_workout_template(db, id)
    except NoResultFound:
        error_response = {
            'message': 'No workout with the given id found'
        }
        return JSONResponse(content=jsonable_encoder(error_response))


@router.post('/exercises')
async def create_exercise_template(createExerciseTemplate: CreateExerciseTemplate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """ create exercise template
    """
    exerciseTemplate = ExerciseTemplate(name=createExerciseTemplate.name)
    newExerciseTemplate = crud.create_exercise_template(db, exerciseTemplate, createExerciseTemplate.workoutTemplateId)
    return newExerciseTemplate


@router.get('/exercises')
async def get_exercise_template(workoutTemplateId: int = None, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """ get exercise templates
    """
    exerciseTemplates = crud.get_exercise_templates(db, workoutTemplateId)
    return exerciseTemplates
