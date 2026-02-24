from typing import Union
from abc import ABC, abstractmethod
from uuid import UUID

from src.models.setting import Setting
from src.schemas.setting import SettingsUpdateRequest


class ISettingRepository(ABC):

	@abstractmethod
	def find_by_user_id(
		self, 
		user_id: UUID
	) -> Union[Setting, None]:
		raise NotImplementedError
		
	@abstractmethod
	def update_by_user_id(
		self,
		user_id: UUID,
		payload: SettingsUpdateRequest
	) -> Union[Setting, None]:
		raise NotImplementedError
