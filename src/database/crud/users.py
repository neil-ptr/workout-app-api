from sqlalchemy.orm import Session
from src.database.database import engine

from src.models.crud import users
from src.database import schemas


def create_user(user: users.UserCreate):
    with Session(engine) as db:
        newUser = schemas.User(
            email=user.email, hashed_password=user.hash, firstname=user.firstname)
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        return newUser


def get_user(user_id: int):
    with Session(engine) as db:
        return db.query(schemas.User).filter(schemas.User.id == user_id).first()


def get_user_by_email(email: str) -> schemas.User:
    with Session(engine) as db:
        return db.query(schemas.User).filter(schemas.User.email == email).first()
