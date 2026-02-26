from fastapi import Request, Response
from fastapi.responses import JSONResponse
from uuid import UUID
from sqlalchemy.orm import Session

from src.schemas.setting import (
	SettingsResponse,
	SettingsUpdateRequest
)
from src.repositories.setting_repository import SettingRepository
import src.services.setting as services


def get_settings(
	request: Request,
	response: Response,
	db: Session,
	user_id: UUID
)  -> JSONResponse:
	
	setting_repo = SettingRepository(db)
	
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


def update_settings(
	request: Request,
	response: Response,
	payload: SettingsUpdateRequest,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	
	setting_repo = SettingRepository(db)

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
