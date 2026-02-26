from typing import List, Union
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.skill_activity import SkillActivity
from src.repositories.interfaces.skill_activity_repository import ISkillActivityRepository
from src.schemas.skill import SkillActivityCreateRequest, SkillActivityUpdateRequest

class SkillActivityRepository(ISkillActivityRepository):

	def __init__(
		self,
		db: Session
	):
		self.db = db

	
	def find_all_by_skill_id(
		self,
		skill_id: UUID
	) -> List[SkillActivity]:
		stmt = select(SkillActivity).where(SkillActivity.skill_id == skill_id)
		activites_data = self.db.scalars(stmt).all()
		return list(activites_data)
	
	def create(
		self,
		skill_id: UUID,
		payload: SkillActivityCreateRequest
	) -> Union[SkillActivity, None]:
		skill_activity_data = SkillActivity(
			**payload.model_dump()
		)
		self.db.add(skill_activity_data)
		self.db.commit()
		self.db.refresh(skill_activity_data)
		return skill_activity_data
		
	def find_by_id(
		self,
		skill_id: UUID
	) -> Union[SkillActivity, None]:
		stmt = select(SkillActivity).where(SkillActivity.id == id)
		skill_activity_data = self.db.scalars(stmt).one_or_none()
		return skill_activity_data
		
	def delete_by_id(
		self,
		skill_id: UUID
	) -> Union[SkillActivity, None]:
		stmt = select(SkillActivity).where(SkillActivity.id == id)
		skill_activity_data = self.db.scalars(stmt).one_or_none()
		self.db.delete(skill_activity_data)
		self.db.commit()
		return skill_activity_data
		
	def update_by_id(
		self,
		skill_id: UUID,
		payload: SkillActivityUpdateRequest
	) -> Union[SkillActivity, None]:
		stmt = select(SkillActivity).where(SkillActivity.id == id)
		skill_activity_data = self.db.scalars(stmt).one_or_none()
		
		updated_payload = payload.model_dump(exclude_none=True, exclude_unset=True)
		for key, value in updated_payload.items():
			setattr(skill_activity_data, key, value)
			
		self.db.commit()
		self.db.refresh(skill_activity_data)
		return skill_activity_data

