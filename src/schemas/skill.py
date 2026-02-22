from pydantic import BaseModel
from datetime import datetime
from typing import Union, List
from uuid import UUID


class SKillActivityResponse(BaseModel):
    id: UUID
    date: datetime
    name: str
    is_completed: bool
    is_priority: bool
    is_habit_to_protect: bool
    minutes_practised: int


class SkillResponse(BaseModel):
    id: UUID
    name: str
    activties: Union[List[SKillActivityResponse], None] = None


class SkillCreateRequest(BaseModel):
    name: str
    activties: Union[List[SKillActivityResponse], None] = None
    

class SkillUpdateRequest(BaseModel):
    name: Union[str, None] = None
    activties: Union[List[SKillActivityResponse], None] = None

