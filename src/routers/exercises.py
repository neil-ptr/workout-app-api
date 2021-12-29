from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.middleware.auth import get_current_user
from src.database import get_db
from src.models.request import exercises
from src.database import crud

router = APIRouter()
