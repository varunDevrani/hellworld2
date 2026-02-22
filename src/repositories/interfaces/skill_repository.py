from typing import List
from abc import ABC, abstractmethod
from uuid import UUID

from src.models.skill import Skill


class ISkillRepository(ABC):

	@abstractmethod
	def find_all_by_user_id(
		self,
		user_id: UUID
	) -> List[Skill]:
		raise NotImplementedError
	
