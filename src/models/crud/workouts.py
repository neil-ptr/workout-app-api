from datetime import datetime
from pydantic import BaseModel


class Workout(BaseModel): 
    started: datetime
    ended: datetime
    active = bool
    workout_template_id = int
