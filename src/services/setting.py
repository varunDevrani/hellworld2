from uuid import UUID

from src.models.setting import Setting
from src.repositories.interfaces.setting_repository import ISettingRepository
from src.exceptions import DomainException, ErrorCode, ErrorDetail, FieldViolation
from src.schemas.setting import SettingsUpdateRequest



def get_settings(
	user_id: UUID,
	setting_repo: ISettingRepository
) -> Setting:
		
	setting_data = setting_repo.find_by_user_id(user_id)
	if setting_data is None:
		raise DomainException(
			404,
			ErrorCode.NOT_FOUND_ERROR,
			"settings not found",
			ErrorDetail(
				resource="settings",
				field_violations=[
					FieldViolation(
						field="settings"
					)
				]
			)
		)
		
	return setting_data
	


def update_settings(
	payload: SettingsUpdateRequest,
	user_id: UUID,
	setting_repo: ISettingRepository
) -> Setting:

	setting_data = setting_repo.update_by_user_id(user_id, payload)
	if setting_data is None:
		raise DomainException(
			404,
			ErrorCode.NOT_FOUND_ERROR,
			"user_id not found",
			ErrorDetail(
				resource="settings",
				field_violations=[
					FieldViolation(
						field="settings"
					)
				]
			)
		)
		
	return setting_data

