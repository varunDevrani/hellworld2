from fastapi import Request, Response
from fastapi.responses import JSONResponse
from uuid import UUID
from sqlalchemy.orm import Session

from src.schemas.user import UserResponse, UserUpdateRequest
from src.repositories.user_repository import UserRepository
from src.schemas.api_response import SuccessResponse
import src.services.user as services



def get_users(
    request: Request,
    response: Response,
    db: Session
) -> JSONResponse:

    user_repo = UserRepository(db)
    users_data = services.get_users(
    	user_repo
    )

    return SuccessResponse(
		status_code=200,
		message="Users fetched successfully.",
		data={
			"total_users": len(users_data),
			"users": [UserResponse.model_validate(data).model_dump(mode="json") for data in users_data]
		}
	)


def get_user_by_id(
    request: Request,
    response: Response,
    user_id: UUID,
    db: Session
) -> JSONResponse:
	
	user_repo = UserRepository(db)
	
	user_data = services.get_user_by_id(
		user_id,
		user_repo
	)
	
	return SuccessResponse(
		status_code=200,
		message=f"User with {user_id} fetched successfully.",
		data={
			"user": UserResponse.model_validate(user_data).model_dump(mode="json")
		}
	)

def update_user_by_id(
	request: Request,
	response: Response,
	payload: UserUpdateRequest,
	user_id: UUID,
	db: Session
) -> JSONResponse:
	
	user_repo = UserRepository(db)

	user_data = services.update_user_by_id(
		payload,
		user_id,
		user_repo
	)
	
	return JSONResponse(
		status_code=200,
		content={
			"success": True,
			"data": {
				"user": UserResponse.model_validate(user_data).model_dump(mode="json")
			}
		}
	)

