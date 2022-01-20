from pydantic import BaseModel
from typing import Optional, Union

from src.models.base.sets import SetsBase


class CreateSet(BaseModel):
    exerciseId: int
    reps: Union[None, int]
    weight: Union[None, float]

class UpdateSet(BaseModel):
    reps: Optional[int]
    weight: Optional[float]
