from uuid import UUID

from src.models.setting import Setting
from src.repositories.interfaces.setting_repository import ISettingRepository
from src.exceptions import AuthenticationError, NotFoundError
from src.schemas.setting import SettingsUpdateRequest



def get_settings(
	user_id: UUID,
	setting_repo: ISettingRepository
) -> Setting:
	
	if user_id is None:
		raise AuthenticationError("invalid token")
		
	setting_data = setting_repo.find_by_user_id(user_id)
	if setting_data is None:
		raise NotFoundError("settings[user_id]")
		
	return setting_data
	


def update_settings(
	payload: SettingsUpdateRequest,
	user_id: UUID,
	setting_repo: ISettingRepository
) -> Setting:
	
	if user_id is None:
		return AuthenticationError("invalid token")

	setting_data = setting_repo.update_by_user_id(user_id, payload)
	if setting_data is None:
		raise NotFoundError("settings[user_id]")
		
	return setting_data

