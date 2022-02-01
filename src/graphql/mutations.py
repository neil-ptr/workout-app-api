import strawberry
import bcrypt
from datetime import timedelta

from src.models.crud.users import UserCreate
from src.config import config
from src.database import crud
from src.utils.jwt import decode_token, sign_token
from .schemas import AuthError, AuthSuccess, AuthResult, Tokens

@strawberry.type
class Mutation:
    @strawberry.field
    def login(self, email: str, password: str) -> AuthResult:
        db_user = crud.get_user_by_email(email)

        if db_user is None:
            return AuthError(message="Email does not exist")

        if not bcrypt.checkpw(password.encode('utf-8'), db_user.hashed_password.encode('utf-8')):
            return AuthError(message="Wrong password")

        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
        access_token = sign_token(
            {"sub": db_user.email}, config.ACCESS_TOKEN_SECRET, config.ACCESS_ALGORITHM, expires_delta=access_token_expires
        )
        refresh_token = sign_token(
            {"sub": db_user.email}, config.REFRESH_TOKEN_SECRET, config.REFRESH_ALGORITHM, expires_delta=refresh_token_expires
        )

        return AuthSuccess(tokens=Tokens(refreshToken=refresh_token, accessToken=access_token))

    @strawberry.field
    def signup(self, email: str, firstname: str, password: str, confirmPassword: str) -> AuthResult:
        db_user = crud.get_user_by_email(email)
        if db_user:
            return AuthError(message="Email already exists")
        if confirmPassword != password:
            return AuthError(message="Passwords do not match")

        hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = UserCreate(hash=hash, firstname=firstname, email=email)
        new_db_user = crud.create_user(new_user)

        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
        access_token = sign_token(
            {"sub": new_db_user.email}, config.ACCESS_TOKEN_SECRET, config.ACCESS_ALGORITHM, expires_delta=access_token_expires
        )
        refresh_token = sign_token(
            {"sub": new_db_user.email}, config.REFRESH_TOKEN_SECRET, config.REFRESH_ALGORITHM, expires_delta=refresh_token_expires
        )
        return AuthSuccess(tokens=Tokens(refreshToken=refresh_token, accessToken=access_token))
