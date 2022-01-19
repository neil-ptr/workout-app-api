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
async def get_sets(exerciseId: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    sets = crud.get_sets(db, exerciseId)
    return sets


@router.post('/')
async def post_sets(createSet: CreateSet, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_set = crud.create_set(db, createSet)
    return JSONResponse(content=jsonable_encoder(new_set))


@router.put('/')
async def update_set(setId: int, updateSet: UpdateSet, db: Session = Depends(get_db), user=Depends(get_current_user)):
    updated = crud.update_set(db, setId, updateSet)
    if updated:
        return 'success'
    else:
        return 'error'


@router.delete('/')
async def delete_set(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'delete set'
