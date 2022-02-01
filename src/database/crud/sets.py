from sqlalchemy.orm import Session

from src.models.crud.sets import Sets
from src.database import schemas, engine


def create_set(db: Session, set: Sets):
    """ create a new set in db

    Args:
        db (Session): database connection
        set (Sets): set data to create new set with

    Returns:
        Set: newly created set
    """
    newSet = schemas.Set(reps=set.reps, weight=set.weight,exercise_id=set.exerciseId)
    db.add(newSet)
    db.commit()
    db.refresh(newSet)
    return newSet

def get_sets(exercise_id: int):
    """ get sets of an exercise

    Args:
        db (Session): database connection
        exercise_id (int): id of the exercise to get sets of 

    Returns:
        List[Set]: List of sets for exercise
    """
    with Session(engine) as db:
        return db.query(schemas.Set) \
            .filter(schemas.Set.exercise_id == exercise_id) \
            .all()


def update_set(db: Session, set_id: int, update_set):
    """ update set with update set data

    Args:
        db (Session): database connection
        set_id (int): id of set to update
        update_set (UpdateSet): data to update set with

    Returns:
        [type]: [description]
    """
    updated = db.query(schemas.Set).filter(
        schemas.Set.id == set_id).update(update_set.dict())
    db.commit()
    return updated


def delete_set(db: Session):
    pass
