from sqlalchemy.orm import Session

from src.database.models import users
from src.database import schemas


def create_user(db: Session, user: users.UserCreate):
    new_user = schemas.User(
        email=user.email, hashed_password=user.hash, firstname=user.firstname)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: int):
    return db.query(schemas.User).filter(schemas.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(schemas.User).filter(schemas.User.email == email).first()
