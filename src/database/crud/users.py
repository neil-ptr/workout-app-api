from sqlalchemy.orm import Session

from src.models.crud import users
from src.database import schemas


def create_user(db: Session, user: users.UserCreate):
    newUser = schemas.User(
        email=user.email, hashed_password=user.hash, firstname=user.firstname)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


def get_user(db: Session, user_id: int):
    return db.query(schemas.User).filter(schemas.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(schemas.User).filter(schemas.User.email == email).first()
