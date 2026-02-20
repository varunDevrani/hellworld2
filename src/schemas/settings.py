from pydantic import BaseModel
from datetime import time
from typing import Union

# settings - general
class GeneralSettingsResponse(BaseModel):
    first_name: str
    last_name: str
    profile_pic_url: str
    morning_start_time: time
    morning_end_time: time
    evening_start_time: time
    evening_end_time: time
    
    
class GeneralSettingsCreateResponse(BaseModel):
    first_name: str
    last_name: str
    profile_pic_url: str
    morning_start_time: time
    morning_end_time: time
    evening_start_time: time
    evening_end_time: time
    
    
class GeneralSettingsUpdateRequest(BaseModel):
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    morning_start_time: Union[time, None] = None
    morning_end_time: Union[time, None] = None
    evening_start_time: Union[time, None] = None
    evening_end_time: Union[time, None] = None
    

# settings - notifications
class NotificationSetingsResponse(BaseModel):
    morning_reminder: bool
    evening_reminder: bool
    

class NotificationSettingsUpdateRequest(BaseModel):
    morning_reminder: Union[bool, None] = None
    evening_reminder: Union[bool, None] = None

