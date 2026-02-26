from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID
from typing import Union

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
	
	def create(
		self,
		user_id: UUID,
		skill_name: str
	) -> Union[Skill, None]:
		skill_data = Skill(
			user_id,
			name=skill_name
		)
		
		self.db.add(skill_data)
		self.db.commit()
		self.db.refresh(skill_data)
		return skill_data
	
	def find_by_id(
		self,
		id: UUID
	) -> Union[Skill, None]:
		stmt = select(Skill).where(Skill.id == id)
		skill_data = self.db.scalars(stmt).one_or_none()
		return skill_data
	
	def delete_by_id(
		self,
		id: UUID
	) -> Union[Skill, None]:
		stmt = select(Skill).where(Skill.id == id)
		skill_data = self.db.scalars(stmt).one_or_none()
		self.db.delete(skill_data)
		self.db.commit()
		return skill_data
		
	def update_by_id(
		self,
		id: UUID,
		skill_name: str
	) -> Union[Skill, None]:
		stmt = select(Skill).where(Skill.id == id)
		skill_data = self.db.scalars(stmt).one_or_none()
		if not skill_data:
			return None
		
		skill_data.name = skill_name
		self.db.commit()
		self.db.refresh(skill_data)
		return skill_data

