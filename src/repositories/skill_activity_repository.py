from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.skill_activity import SkillActivity
from src.repositories.interfaces.skill_activity_repository import ISkillActivityRepository


class SkillActivityRepository(ISkillActivityRepository):

	def __init__(
		self,
		db: Session
	):
		self.db = db

	
	def find_activities_by_skill_id(
		self,
		skill_id: UUID
	) -> List[SkillActivity]:
		
		stmt = select(SkillActivity).where(SkillActivity.skill_id == skill_id)
		activites_data = self.db.scalars(stmt).all()

		return list(activites_data)