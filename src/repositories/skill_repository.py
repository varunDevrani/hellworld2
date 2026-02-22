from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID

from src.models.skill import Skill
from src.repositories.interfaces.skill_repository import ISkillRepository


class SkillRepository(ISkillRepository):

	def __init__(
		self,
		db: Session
	):
		self.db = db

	
	def find_all_by_user_id(
		self,
		user_id: UUID
	) -> List[Skill]:

		stmt = select(Skill).where(Skill.user_id == user_id)
		skills_data = self.db.scalars(stmt).all()

		return list(skills_data)