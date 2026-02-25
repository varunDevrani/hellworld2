from fastapi import Request, Response
from fastapi.responses import JSONResponse
from uuid import UUID
from sqlalchemy.orm import Session

from src.schemas.setting import (
	SettingsResponse,
	SettingsUpdateRequest
)
from src.repositories.setting_repository import SettingRepository
from src.exceptions import NotFoundError, AuthenticationError
import src.services.setting as services


def get_settings(
	request: Request,
	response: Response,
	db: Session,
	user_id: UUID
)  -> JSONResponse:
	
	setting_repo = SettingRepository(db)
	
	try:
		setting_data = services.get_settings(
			user_id,
			setting_repo
		)
		
		response.status_code = 200
		return JSONResponse(
			status_code=200,
			content={
				"success": True,
				"data": {
					"settings": SettingsResponse.model_validate(setting_data).model_dump(mode="json")
				}
			}
		)
	except AuthenticationError as exception:
		response.status_code = 401
		return JSONResponse(
			status_code=401,
			content={
				"success": False,
				"content": {
					"code": "AUTHENTICATION_ERROR",
					"message": exception.message,
					"details": {
						"field": "user_id"
					}
				}
			}
		)
	except NotFoundError as exception:
		response.status_code = 404
		return JSONResponse(
			status_code=404,
			content={
				"success": False,
				"content": {
					"code": "NOT_FOUND",
					"message": exception.message,
					"details": {
						"field": "user_id"
					}
				}
			}
		)


def update_settings(
	request: Request,
	response: Response,
	payload: SettingsUpdateRequest,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	
	setting_repo = SettingRepository(db)

	try:
		setting_data = services.update_settings(
			payload,
			user_id,
			setting_repo
		)
		
		response.status_code = 200
		return JSONResponse(
			status_code=200,
			content={
				"success": True,
				"data": {
					"settings": SettingsResponse.model_validate(setting_data).model_dump(mode="json")
				}
			}
		)
	except AuthenticationError as exception:
		response.status_code = 401
		return JSONResponse(
			status_code=401,
			content={
				"success": False,
				"content": {
					"code": "AUTHENTICATION_ERROR",
					"message": exception.message,
					"details": {
						"field": "user_id"
					}
				}
			}
		)
	except NotFoundError as exception:
		response.status_code = 404
		return JSONResponse(
			status_code=404,
			content={
				"success": False,
				"content": {
					"code": "NOT_FOUND",
					"message": exception.message,
					"details": {
						"field": "user_id"
					}
				}
			}
		)
