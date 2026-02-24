from fastapi import Request, Response
from fastapi.responses import JSONResponse
from uuid import UUID
from sqlalchemy.orm import Session

from src.schemas.user import UserResponse
from src.repositories.user_repository import UserRepository
from src.exceptions import NotFoundError
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

    response.status_code = 200
    return JSONResponse(
		status_code=200,
		content={
			"success": True,
			"data": {
			    "total_users": len(users_data),
				"users": [UserResponse.model_validate(data).model_dump(mode="json") for data in users_data]
			}
		}
	)


def get_user_by_id(
    request: Request,
    response: Response,
    user_id: UUID,
    db: Session
) -> JSONResponse:
	
	user_repo = UserRepository(db)
	
	try:
		user_data = services.get_user_by_id(
			user_id,
			user_repo
		)
		
		response.status_code = 200
		return JSONResponse(
			status_code=200,
			content={
				"success": True,
				"content": {
					"user": UserResponse.model_validate(user_data).model_dump(mode="json")
				}
			}
		)
	except NotFoundError as exception:
		response.status_code = 404
		return JSONResponse(
			status_code=200,
			content={
				"success": True,
				"content": {
					"success": False,
					"code": "NOT_FOUND",
					"message": exception.message,
					"details": {
						"field": "user_id"
					}
				}
			}
		)
