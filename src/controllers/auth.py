from typing import Union
from fastapi import Request, Response
from sqlalchemy.orm import Session

from src.schemas.user import UserResponse
from src.schemas.auth import SignupRequest, LoginRequest, RefreshTokenRequest
from src.schemas.api_response import SuccessResponse, ErrorResponse
from src.repositories.user_repository import UserRepository
from src.repositories.refresh_token_repository import RefreshTokenRepository
from src.exceptions import ConflictError, ValidationError, AuthenticationError, InvalidRefreshTokenError

import src.services.auth as services


def signup(
	request: Request,
	response: Response,
	payload: SignupRequest,
	db: Session
) -> Union[SuccessResponse, ErrorResponse]:
	
	user_repo = UserRepository(db)
	
	try:
		user_data = services.signup(
			payload,
			user_repo
		)

		response.status_code = 201
		return SuccessResponse(
			message="user created. please log in",
			status_code=201,
			data={
				"user": UserResponse.model_validate(user_data)
			}
		)

	except ValidationError as exception:
		response.status_code = 400
		return ErrorResponse(
			message=exception.message,
			status_code=400,
		)	
	
	except ConflictError as exception:
		response.status_code = 409
		return ErrorResponse(
			message=exception.message,
			status_code=409,
		)


def login(
	request: Request,
	response: Response,
	payload: LoginRequest,
	db: Session
) -> Union[SuccessResponse, ErrorResponse]:
	
	user_repo = UserRepository(db)
	refresh_token_repo = RefreshTokenRepository(db)
	
	try:
		token_data = services.login(
			payload,
			user_repo,
			refresh_token_repo
		)

		response.status_code = 200
		return SuccessResponse(
			message="user logged in",
			status_code=200,
			data=token_data
		)

	except AuthenticationError as exception:
		response.status_code = 401
		return ErrorResponse(
			message=exception.message,
			status_code=401,
		)
	
	except ConflictError as exception:
		response.status_code = 409
		return ErrorResponse(
			message=exception.message,
			status_code=409,
		)


def refresh(
	request: Request,
	response: Response,
	payload: RefreshTokenRequest,
	db: Session
) -> Union[SuccessResponse, ErrorResponse]:

	refresh_token_repo = RefreshTokenRepository(db)

	try:
		token_data = services.refresh(
			payload,
			refresh_token_repo
		)

		response.status_code = 200
		return SuccessResponse(
			message="new access token generated",
			status_code=200,
			data=token_data
		)
	
	except InvalidRefreshTokenError as exception:
		response.status_code = 401
		return ErrorResponse(
			message=exception.message,
			status_code=409,
		)


def logout(
	request: Request,
	response: Response,
	payload: RefreshTokenRequest,
	db: Session
):
	refresh_token_repo = RefreshTokenRepository(db)

	try:
		services.logout(
			payload,
			refresh_token_repo
		)

		response.status_code = 200
		return SuccessResponse(
			message="logged out",
			status_code=200,
		)
	
	except InvalidRefreshTokenError as exception:
		response.status_code = 401
		return ErrorResponse(
			message=exception.message,
			status_code=409,
		)

