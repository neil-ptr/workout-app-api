from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.database.crud import *
from src.database import get_db

router = APIRouter()


@router.get("/users/{user_id}")
async def get_user(db: Session = Depends(get_db)):
    pass
