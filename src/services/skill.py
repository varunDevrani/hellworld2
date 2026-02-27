from uuid import UUID
from typing import List, Dict, Any

from src.repositories.interfaces.skill_repository import ISkillRepository
from src.repositories.interfaces.skill_activity_repository import ISkillActivityRepository
from src.exceptions import DomainException, ErrorCode, ErrorDetail, FieldViolation
from src.schemas.skill import SkillActivityCreateRequest, SkillCreateRequest, SkillUpdateRequest

def get_skills(
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
) -> List[Dict[str, Any]]:

	result = []
	skills_data = skill_repo.find_all_by_user_id(user_id)

	for skill in skills_data:
		result.append({
			"id": skill.id,
			"skill_name": skill.name,
			"activities": skill_activity_repo.find_all_by_skill_id(skill.id)
		})

	return result


def create_skill(
	payload: SkillCreateRequest,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	skill_data = skill_repo.create(payload.name)
	if skill_data is None:
		raise DomainException(
			500,
			ErrorCode.INTERNAL_SERVER_ERROR,
			"Failed to create resource",
			ErrorDetail(
				resource="skills"
			)
		)
		
	if payload.activities is None:
		return skill_data
	
	activities = []	
	for activity in payload.activities:
		activity_data = skill_activity_repo.create(
			skill_data.id,
			activity
		)
		activities.append(activity_data)
	
	return {
		"skill": skill_data,
		"activities": activities
	}


def delete_skill_by_id(
	skill_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
):
	skill_data = skill_repo.delete_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			500,
			ErrorCode.INTERNAL_SERVER_ERROR,
			"Failed to create resource",
			ErrorDetail(
				resource="skills"
			)
		)
	return skill_data


def update_skill_by_id(
	payload: SkillUpdateRequest,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	pass


def get_skill_by_id(
	skill_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			404,
			ErrorCode.NOT_FOUND_ERROR,
			"Failed to create resource",
			ErrorDetail(
				resource="skills"
			)
		)

	return {
		"skill": skill_data,
		"activities": skill_activity_repo.find_all_by_skill_id(skill_data.id)
	}


def create_skill_activity(
	skill_id: UUID,
	user_id: UUID,
	payload: SkillActivityCreateRequest,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	skill_activity_data = skill_activity_repo.create(skill_id, payload)
	


def get_skill_activity_by_id(
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	pass


def delete_skill_activity_by_id(
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID,
	skill_activity_repo: ISkillActivityRepository
):
	pass


def update_skill_activity_by_id(
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	pass


