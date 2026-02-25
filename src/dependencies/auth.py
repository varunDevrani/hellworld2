from uuid import UUID
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.utils.jwt_handler import JWTToken, decode_token
from src.exceptions import DomainException, ErrorCode, ErrorDetail



security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> UUID:
    
	if not credentials:
		raise DomainException(
			401,
			ErrorCode.AUTHENTICATION_ERROR,
			"Invalid Credentials",
			ErrorDetail(
				resource="users"
			)
		)
    
	token = decode_token(credentials.credentials)
	
	if token is None or token.token_type != JWTToken.ACCESS_TOKEN:
		raise DomainException(
			401,
			ErrorCode.AUTHENTICATION_ERROR,
			"Invalid Credentials",
			ErrorDetail(
				resource="users"
			)
		)
	
	return UUID(token.user_id)
