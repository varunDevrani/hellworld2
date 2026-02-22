from typing import Dict, Any
from uuid import UUID

from src.models.user import User
from src.utils.hash import hash_password, verify_password
from src.exceptions import ConflictError, ValidationError, AuthenticationError, InvalidRefreshTokenError
from src.schemas.auth import SignupRequest, LoginRequest, RefreshTokenRequest
from src.repositories.interfaces.user_repository import IUserRepository
from src.repositories.interfaces.refresh_token_repository import IRefreshTokenRepository
from src.utils.jwt_handler import JWTToken, create_token, decode_token


def signup(
	payload: SignupRequest,
	user_repo: IUserRepository
) -> User:
	
	if payload.password != payload.confirm_password:
		raise ValidationError("password and confirm_password do not match")
	
	user_data = user_repo.find_by_email(payload.email)

	if user_data is not None:
		raise ConflictError("email already exists")
	
	user_data = user_repo.create(
		email=payload.email,
		password_hash=hash_password(payload.password)
	)
	
	return user_data


def login(
	payload: LoginRequest,
	user_repo: IUserRepository,
	refresh_token_repo: IRefreshTokenRepository
) -> Dict[str, Any]:
	
	user_data = user_repo.find_by_email(payload.email)

	if user_data is None:
		raise AuthenticationError("invalid credentials")
	
	if not verify_password(payload.password, user_data.password_hash):
		raise AuthenticationError("invalid credentials")
	
	refresh_token_data = refresh_token_repo.find_by_used_id(user_data.id)
	if refresh_token_data is not None:
		raise ConflictError("user is already logged in")
	
	access_token_payload, access_token = create_token(user_data.id, JWTToken.ACCESS_TOKEN)
	refresh_token_payload, refresh_token = create_token(user_data.id, JWTToken.REFRESH_TOKEN)

	refresh_token_repo.create(
		user_data.id,
		refresh_token,
		refresh_token_payload.iat,
		refresh_token_payload.exp
	)

	return {
		"type": "bearer",
		"access_token": access_token,
		"refresh_token": refresh_token
	}


def refresh(
	payload: RefreshTokenRequest,
	refresh_token_repo: IRefreshTokenRepository
) -> Dict[str, Any]:
	
	token_data = refresh_token_repo.find_by_token(payload.refresh_token)
	if token_data is None:
		raise InvalidRefreshTokenError("invalid refresh token")
	
	refresh_token_payload = decode_token(token_data.token)
	if refresh_token_payload is None:
		raise InvalidRefreshTokenError("invalid refresh token")

	access_token_payload, access_token = create_token(UUID(refresh_token_payload.user_id), JWTToken.ACCESS_TOKEN)

	return {
		"type": "bearer",
		"access_token": access_token
	}


def logout(
	payload: RefreshTokenRequest,
	refresh_token_repo: IRefreshTokenRepository
):
	
	token_data = refresh_token_repo.find_by_token(payload.refresh_token)
	if token_data is None:
		raise InvalidRefreshTokenError("invalid refresh token")
	
	refresh_token_repo.delete_token(token_data)
