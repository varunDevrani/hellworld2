import jwt

from pydantic import BaseModel
from enum import Enum
from uuid import UUID
from datetime import datetime, timezone, timedelta
from typing import Tuple, Union

from src.core.config import (
    JWT_SECRET_KEY,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS,
    OTP_CODE_EXPIRE_MINUTES
)


class JWTToken(str, Enum):
    ACCESS_TOKEN = "access"
    REFRESH_TOKEN = "refresh"
    OTP_TOKEN = "otp"
    

class JWTPayload(BaseModel):
    user_id: str
    exp: datetime
    iat: datetime
    token_type: str
    
    
ALGORITHM = "HS256"

    
def create_token(
    user_id: UUID, 
    token_type: JWTToken
) -> Tuple[JWTPayload, str]:
    
    match token_type:
        case JWTToken.ACCESS_TOKEN:
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        case JWTToken.REFRESH_TOKEN:
            expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        case JWTToken.OTP_TOKEN:
            expire = datetime.now(timezone.utc) + timedelta(minutes=OTP_CODE_EXPIRE_MINUTES)
        case _:
            raise ValueError("Not a valid token type!")
            
    
    payload: JWTPayload = JWTPayload(
        user_id=str(user_id),
        exp=expire,
        iat=datetime.now(timezone.utc),
        token_type=token_type.value
    )
    
    return (payload, jwt.encode(payload.model_dump(), JWT_SECRET_KEY, ALGORITHM))
    
    
def decode_token(
    token: str
) -> Union[JWTPayload, None]:
    
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, [ALGORITHM])
        return JWTPayload(**payload)
    except jwt.PyJWTError as exception:
        return None

