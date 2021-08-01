import os
import bcrypt
from fastapi import Depends, APIRouter, Response, status, Cookie
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv, find_dotenv
from typing import Optional

from src.models.request.users import Login, SignUp
from src.database.crud import *
from src.database import SessionLocal, engine, get_db
from src.models.crud.users import UserCreate, UserBase
from src.utils import create_access_token
from src.models.response import token
from src.middleware import auth

router = APIRouter()

load_dotenv(find_dotenv())
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")


@router.post("/token", response_model=token.Token)
async def login_user(user: Login, response: Response, db: Session = Depends(get_db)):
    print('jdkflsdj')
    try:
        dbUser = get_user_by_email(db, user.email)
        if not dbUser:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=jsonable_encoder({'error': 'User not found'}))
        if not bcrypt.checkpw(user.password.encode('utf-8'), dbUser.hashed_password.encode('utf-8')):
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=jsonable_encoder({'error': 'Incorrect password'}))
        access_token_expires = timedelta(
            minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        response.set_cookie(
            key="token", value=f"bearer {access_token}", samesite="strict", httponly=True)
    except Exception as e:
        raise(e)


@router.post("/signup", response_model=token.Token)
async def signup_user(user: SignUp, response: Response, db: Session = Depends(get_db)):
    dbUser = get_user_by_email(db, user.email)
    print(dbUser)
    if dbUser:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content='Email exists')
    hash = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = UserCreate(
        hash=hash, firstname=user.firstname, email=user.email)
    db_user = create_user(db, new_user)
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="token", value=f"bearer {access_token}", samesite="strict", httponly=True)
