from uuid import UUID
from typing import Union
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.schemas.api_response import ErrorResponse
from src.utils.jwt_handler import JWTToken, decode_token


security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> Union[UUID, ErrorResponse]:
    
	if not credentials:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="not authenticated"
		)
    
	token = decode_token(credentials.credentials)
	
	if token is None or token.token_type != JWTToken.ACCESS_TOKEN:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="invalid token"
		)
	
	return UUID(token.user_id)
