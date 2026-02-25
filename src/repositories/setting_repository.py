from typing import Union
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.setting import Setting
from src.repositories.interfaces.setting_repository import ISettingRepository
from src.schemas.setting import SettingsUpdateRequest


class SettingRepository(ISettingRepository):
	
	def __init__(
		self,
		db: Session
	):
		self.db = db

	def find_by_user_id(
		self, 
		user_id: UUID
	) -> Union[Setting, None]:
		stmt = select(Setting).where(Setting.user_id == user_id)
		setting_data = self.db.scalar(stmt)
		return setting_data
		
	def update_by_user_id(
		self,
		user_id: UUID,
		payload: SettingsUpdateRequest
	) -> Union[Setting, None]:
		
		setting_data = self.find_by_user_id(user_id)
		
		if not setting_data:
			return None
			
		updated_payload = payload.model_dump(exclude_unset=True, exclude_none=True)
		for key, value in updated_payload.items():
			setattr(setting_data, key, value)
			
		self.db.commit()
		self.db.refresh(setting_data)
		return setting_data
		
