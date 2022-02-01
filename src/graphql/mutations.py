import strawberry
import bcrypt
from datetime import timedelta

from src.config import config
from src.database import crud
from src.utils.jwt import decode_token, sign_token
from .schemas import LoginError, LoginSuccess, LoginResult, Tokens

@strawberry.type
class Mutation:
    @strawberry.field
    def login(self, email: str, password: str) -> LoginResult:

        db_user = crud.get_user_by_email(email)

        if db_user is None:
            return LoginError(message="Email does not exist")

        if not bcrypt.checkpw(password.encode('utf-8'), db_user.hashed_password.encode('utf-8')):
            return LoginError(message="Wrong password")

        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
        access_token = sign_token(
            {"sub": db_user.email}, config.ACCESS_TOKEN_SECRET, config.ACCESS_ALGORITHM, expires_delta=access_token_expires
        )
        refresh_token = sign_token(
            {"sub": db_user.email}, config.REFRESH_TOKEN_SECRET, config.REFRESH_ALGORITHM, expires_delta=refresh_token_expires
        )

        return LoginSuccess(tokens=Tokens(refreshToken=refresh_token, accessToken=access_token))