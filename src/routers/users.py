import os
import bcrypt
from fastapi import Depends, APIRouter, Response, status, Cookie
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv, find_dotenv
from typing import Optional

from src.models.request.users import Login, SignUp
from src.database.crud import *
from src.database import SessionLocal, engine, get_db
from src.database.models.users import UserCreate, UserBase
from src.utils import create_access_token
from src.models.response import token
from src.middleware import auth

router = APIRouter()

load_dotenv(find_dotenv())
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")


@router.post("/token", response_model=token.Token)
async def login_user(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_email(db, form_data.username)
    if not user:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content='User not found')
    if not bcrypt.checkpw(form_data.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content='Incorrect password')
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", response_model=token.Token)
async def signup_user(user: SignUp, db: Session = Depends(get_db)):
    dbUser = get_user_by_email(db, user.email)
    if dbUser:
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content='Email exists')
    hash = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = UserCreate(
        hash=hash, firstname=user.firstname, email=user.email)
    db_user = create_user(db, new_user)
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
