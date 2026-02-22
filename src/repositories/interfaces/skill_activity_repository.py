from typing import List
from abc import ABC, abstractmethod
from uuid import UUID

from src.models.skill_activity import SkillActivity


class ISkillActivityRepository(ABC):

	@abstractmethod
	def find_activities_by_skill_id(
		self,
		skill_id: UUID
	) -> List[SkillActivity]:
		raise NotImplementedError
	
