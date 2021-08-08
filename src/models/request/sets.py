from pydantic import BaseModel
from typing import Optional

from src.models.base.sets import SetsBase


class CreateSet(SetsBase):
    exerciseId: int


class UpdateSet(BaseModel):
    reps: Optional[int]
    weight: Optional[float]
