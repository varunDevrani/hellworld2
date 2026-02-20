from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import Union, Dict, Any

class Meta(BaseModel):
    request_id: UUID
    timestamp: datetime


class APIResponse(BaseModel):
    message: str = "request processed"
    success: bool
    status_code: int
    meta: Union[Meta, None] = None

class SuccessResponse(APIResponse):
    success: bool = True
    data: Union[Dict[str, Any], None] = None
  
class ErrorResponse(APIResponse):
    success: bool = False
    errors: Union[Dict[str, Any], None] = None    

