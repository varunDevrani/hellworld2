from pydantic import BaseModel
from datetime import datetime
from typing import Union, List


class ActivityResponse(BaseModel):
    date: datetime
    name: str
    is_completed: bool
    is_priority: bool
    is_habit_to_protect: bool
    minutes_practised: int


class SkillResponse(BaseModel):
    name: str
    activties: Union[List[ActivityResponse], None] = None


class SkillCreateRequest(BaseModel):
    name: str
    activties: Union[List[ActivityResponse], None] = None
    

class SkillUpdateRequest(BaseModel):
    name: Union[str, None] = None
    activties: Union[List[ActivityResponse], None] = None

