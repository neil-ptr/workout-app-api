from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Workout(BaseModel): 
    started: datetime
    ended: Optional[datetime]
    active = bool
