
import os
from fastapi import HTTPException, Depends, status
from jose import JWTError, jwt
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.orm import Session

from src.auth.cookie_auth import CookieAuthScheme
from src.database import get_db
from src.database.crud import get_user_by_email


load_dotenv(find_dotenv())
ALGORITHM = os.environ.get("ALGORITHM")
SECRET_KEY = os.environ.get("SECRET_KEY")

cookieAuth = CookieAuthScheme()


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(cookieAuth)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, username)
    if user is None:
        raise credentials_exception
    return user
