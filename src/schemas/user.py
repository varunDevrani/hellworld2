from typing import Union
from uuid import UUID
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: UUID
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    email: str
    profile_pic_url: Union[str, None] = None


class UserCreateRequest(BaseModel):
    email: str
    password: str
    confirm_password: str

