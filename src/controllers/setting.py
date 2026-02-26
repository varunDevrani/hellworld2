from fastapi import Request, Response
from fastapi.responses import JSONResponse
from uuid import UUID
from sqlalchemy.orm import Session

from src.schemas.setting import (
	SettingsResponse,
	SettingsUpdateRequest
)
from src.repositories.setting_repository import SettingRepository
from src.schemas.api_response import SuccessResponse
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
	
	return SuccessResponse(
		status_code=200,
		message="Settings[user_id] fetched successfully.",
		data={
			"settings": SettingsResponse.model_validate(setting_data).model_dump(mode="json")
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
	
	return SuccessResponse(
		status_code=200,
		message="Settings[user_id] updated successfully.",
		data={
			"settings": SettingsResponse.model_validate(setting_data).model_dump(mode="json")
		}
	)	
	
