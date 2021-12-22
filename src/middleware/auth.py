from fastapi import HTTPException, Depends, status
from jose.exceptions import JWTError
from sqlalchemy.orm import Session
from src.auth.header_auth import header_auth

from src.database import get_db
from src.database.crud import get_user_by_email


async def get_current_user(db: Session = Depends(get_db), payload: str = Depends(header_auth)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception
        user = get_user_by_email(db, email)

        if user is None:
            raise credentials_exception
        return user

    except JWTError:
        raise credentials_exception
