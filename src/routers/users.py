import bcrypt
from fastapi import Depends, APIRouter, Response, status
from sqlalchemy.orm import Session

from src.models.request.users import Login, SignUp
from src.database.crud import *
from src.database import SessionLocal, engine
from src.database.models.users import UserCreate, UserBase

router = APIRouter()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/users/login')
async def login_user(user: Login, db: Session = Depends(get_db)):
    dbUser = get_user_by_email(db, user.email)
    if not dbUser:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content='User not found')
    if bcrypt.checkpw(user.password.encode('utf-8'), dbUser.hashed_password.encode('utf-8')):
        return Response(status_code=status.HTTP_200_OK, content='User found')
    else:
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content='Incorrect password')


@router.post('/users/signup')
async def signup_user(user: SignUp, db: Session = Depends(get_db)):
    dbUser = get_user_by_email(db, user.email)

    if dbUser:
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content='Email exists')

    hash = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    newUser = UserCreate(hash=hash, firstname=user.firstname, email=user.email)
    create_user(db, newUser)
