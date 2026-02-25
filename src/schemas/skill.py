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

class SkillActivityCreateRequest(BaseModel):
	name: str
	is_completed: bool = False
	is_priority: bool = False
	is_habit_to_protect: bool = False
	minutes_practised: int = 0

class SkillActivityUpdateRequest(BaseModel):
	name: Union[str, None] = None
	is_completed: Union[bool, None] = None
	is_priority: Union[bool, None] = None
	is_habit_to_protect: Union[bool, None] = None
	minutes_practised: Union[int, None] = None
	

class SkillResponse(BaseModel):
    id: UUID
    name: str
    total_activites: int
    activties: Union[List[SKillActivityResponse], None] = None

class SkillCreateRequest(BaseModel):
    name: str
    activties: Union[List[SKillActivityResponse], None] = None
    
class SkillUpdateRequest(BaseModel):
    name: Union[str, None] = None
    activties: Union[List[SKillActivityResponse], None] = None

class SkillsResponse(BaseModel):
	total_skills: int
	skills: Union[List[SkillResponse], None] = None

