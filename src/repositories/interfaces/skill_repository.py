from typing import List
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Union

from src.models.skill import Skill


class ISkillRepository(ABC):
	
	@abstractmethod
	def find_all_by_user_id(
		self,
		user_id: UUID
	) -> List[Skill]:
		raise NotImplementedError
	
	@abstractmethod
	def create(
		self,
		user_id: UUID,
		skill_name: str
	) -> Union[Skill, None]:
		raise NotImplementedError
	
	@abstractmethod
	def find_by_id(
		self,
		id: UUID
	) -> Union[Skill, None]:
		raise NotImplementedError
	
	@abstractmethod
	def delete_by_id(
		self,
		id: UUID
	) -> Union[Skill, None]:
		raise NotImplementedError
		
	@abstractmethod
	def update_by_id(
		self,
		id: UUID,
		skill_name: str
	) -> Union[Skill, None]:
		raise NotImplementedError

