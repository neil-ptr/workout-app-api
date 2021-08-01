from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.middleware.auth import get_current_user
from src.models.request.sets import CreateSet
from src.database.crud import sets as crud

router = APIRouter()


@router.get('/')
async def get_sets(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'get sets'


@router.post('/')
async def post_sets(set: CreateSet, db: Session = Depends(get_db), user=Depends(get_current_user)):
    newSet = crud.create_set(db, set)
    print(newSet)
    return 'post sets'


@router.put('/')
async def update_set(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'get set'


@router.delete('/')
async def delete_set(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return 'delete set'
