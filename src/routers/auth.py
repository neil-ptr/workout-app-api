from datetime import timedelta
import bcrypt

from fastapi import Depends, APIRouter, status
from fastapi.exceptions import HTTPException
from jose.exceptions import JWTError
from src.models.request.users import Login, SignUp, RefreshToken
from src.database.crud import *
from src.database import get_db
from src.models.crud.users import UserCreate
from src.config import config
from src.utils.jwt import decode_token, sign_token

router = APIRouter()


@router.post('/signup')
async def signup(user: SignUp, db: Session = Depends(get_db)):
    """ save new user in database
    """
    db_user = get_user_by_email(db, user.email)
    if db_user:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content='Email exists')
    hash = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = UserCreate(
        hash=hash, firstname=user.firstname, email=user.email)
    new_db_user = create_user(db, new_user)

    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
    access_token = sign_token(
        {"sub": new_db_user.email}, config.ACCESS_TOKEN_SECRET, config.ACCESS_ALGORITHM, expires_delta=access_token_expires
    )
    refresh_token = sign_token(
        {"sub": new_db_user.email}, config.REFRESH_TOKEN_SECRET, config.REFRESH_ALGORITHM, expires_delta=refresh_token_expires
    )
    return JSONResponse(content=jsonable_encoder({
        "access_token": access_token,
        "refresh_token": refresh_token
    }))


@router.post('/tokens')
async def tokens(user: Login, db: Session = Depends(get_db)):
    """ get new access and refresh tokens after authenticating credentials
    """
    db_user = get_user_by_email(db, user.email)
    if not db_user:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=jsonable_encoder({'error': 'User not found'}))
    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.hashed_password.encode('utf-8')):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=jsonable_encoder({'error': 'Incorrect password'}))

    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
    access_token = sign_token(
        {"sub": db_user.email}, config.ACCESS_TOKEN_SECRET, config.ACCESS_ALGORITHM, expires_delta=access_token_expires
    )
    refresh_token = sign_token(
        {"sub": db_user.email}, config.REFRESH_TOKEN_SECRET, config.REFRESH_ALGORITHM, expires_delta=refresh_token_expires
    )
    return JSONResponse(content=jsonable_encoder({
        "access_token": access_token,
        "refresh_token": refresh_token
    }))


@router.post('/refreshToken')
async def refresh_token(refreshToken: RefreshToken, db: Session = Depends(get_db)):
    """ sign a new access token if refresh token is still valid
    """
    try:
        payload = decode_token(refreshToken.refreshToken, config.REFRESH_TOKEN_SECRET, config.REFRESH_ALGORITHM)
        db_user = get_user_by_email(db, payload['sub'])

        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
        access_token = sign_token(
            {"sub": db_user.email}, config.ACCESS_TOKEN_SECRET, config.ACCESS_ALGORITHM, expires_delta=access_token_expires
        )
        refresh_token = sign_token(
            {"sub": db_user.email}, config.REFRESH_TOKEN_SECRET, config.REFRESH_ALGORITHM, expires_delta=refresh_token_expires
        )
        return JSONResponse(content=jsonable_encoder({
            "access_token": access_token,
            "refresh_token": refresh_token
        }))
    except JWTError:
        return HTTPException()
