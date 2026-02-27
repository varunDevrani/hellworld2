from typing import List
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Union

from src.models.skill_activity import SkillActivity
from src.schemas.skill import SkillActivityCreateRequest, SkillActivityUpdateRequest


class ISkillActivityRepository(ABC):

	@abstractmethod
	def find_all_by_skill_id(
		self,
		skill_id: UUID
	) -> List[SkillActivity]:
		raise NotImplementedError
	
	@abstractmethod
	def create(
		self,
		skill_id: UUID,
		payload: SkillActivityCreateRequest
	) -> Union[SkillActivity, None]:
		raise NotImplementedError
		
	@abstractmethod
	def find_by_id(
		self,
		skill_id: UUID
	) -> Union[SkillActivity, None]:
		raise NotImplementedError
		
	@abstractmethod
	def delete_by_id(
		self,
		skill_id: UUID
	) -> Union[SkillActivity, None]:
		raise NotImplementedError
		
	@abstractmethod
	def update_by_id(
		self,
		skill_id: UUID,
		payload: SkillActivityUpdateRequest
	) -> Union[SkillActivity, None]:
		raise NotImplementedError

