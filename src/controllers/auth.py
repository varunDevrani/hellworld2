from fastapi import Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.schemas.user import UserResponse
from src.schemas.auth import SignupRequest, LoginRequest, RefreshTokenRequest
from src.schemas.api_response import SuccessResponse
from src.repositories.user_repository import UserRepository
from src.repositories.refresh_token_repository import RefreshTokenRepository

import src.services.auth as services


def signup(
	request: Request,
	response: Response,
	payload: SignupRequest,
	db: Session
) -> JSONResponse:
	
	user_repo = UserRepository(db)
	
	user_data = services.signup(
		payload,
		user_repo
	)

	return SuccessResponse(
		status_code=201,
		message="user created. please log in",
		data={
			"user": UserResponse.model_validate(user_data)
		}
	)


def login(
	request: Request,
	response: Response,
	payload: LoginRequest,
	db: Session
) -> JSONResponse:
	
	user_repo = UserRepository(db)
	refresh_token_repo = RefreshTokenRepository(db)
	
	token_data = services.login(
		payload,
		user_repo,
		refresh_token_repo
	)

	return SuccessResponse(
		status_code=200,
		message="User logged in. Verify OTP from mail.",
		data={
			"user": token_data
		}
	)


def refresh(
	request: Request,
	response: Response,
	payload: RefreshTokenRequest,
	db: Session
) -> JSONResponse:

	refresh_token_repo = RefreshTokenRepository(db)

	token_data = services.refresh(
		payload,
		refresh_token_repo
	)

	return SuccessResponse(
		status_code=200,
		message="New access token generated.",
		data={
			"user": token_data
		}
	)
	

def logout(
	request: Request,
	response: Response,
	payload: RefreshTokenRequest,
	db: Session
):
	refresh_token_repo = RefreshTokenRepository(db)

	services.logout(
		payload,
		refresh_token_repo
	)

	return SuccessResponse(
		status_code=200,
		message="User logged out."
	)
