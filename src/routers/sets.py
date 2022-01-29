from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.database import get_db
from src.middleware.auth import get_current_user
from src.models.request.sets import CreateSet, UpdateSet
from src.database.crud import sets as crud

router = APIRouter()


@router.get('/')
async def get_sets(exerciseId: int = None, workoutId: int = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if workoutId:
        return crud.get_sets_by_workout_id(db, workoutId)
    else:
        return crud.get_sets(db, exerciseId)


@router.post('/')
async def post_sets(create_set: CreateSet, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_set = crud.create_set(db, create_set)
    return JSONResponse(content=jsonable_encoder(new_set))


@router.put('/{set_id}')
async def update_set(set_id: int, update_set: UpdateSet, db: Session = Depends(get_db), user=Depends(get_current_user)):
    updated = crud.update_set(db, set_id, update_set)
    if updated:
        return 'success'
    else:
        # TODO: return better error
        return 'error'


@router.delete('/')
async def delete_set(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'delete set'
