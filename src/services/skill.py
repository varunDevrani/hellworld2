from uuid import UUID
from typing import List, Dict, Any

from src.repositories.interfaces.skill_repository import ISkillRepository
from src.repositories.interfaces.skill_activity_repository import ISkillActivityRepository
from src.exceptions import DomainException, ErrorCode, ErrorDetail, FieldViolation
from src.schemas.skill import SkillCreateRequest, SkillUpdateRequest

def get_skills(
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
) -> List[Dict[str, Any]]:
	
	if user_id is None:
		raise DomainException(
			401,
			ErrorCode.AUTHENTICATION_ERROR,
			"Invalid Token",
			ErrorDetail(
				resource="skills",
				field_violations=[
					FieldViolation(
						field="token[user_id]"
					)
				]
			)
		)

	result = []
	skills_data = skill_repo.find_all_by_user_id(user_id)
	print(f"SKILL DATA: {skills_data}")

	for skill in skills_data:
		result.append({
			"id": skill.id,
			"skill_name": skill.name,
			"activities": skill_activity_repo.find_activities_by_skill_id(skill.id)
		})

	return result


def create_skill(
	payload: SkillCreateRequest,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	pass


def delete_skill_by_id(
	skill_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
):
	pass


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
	pass


def create_skill_activity(
	skill_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	pass


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


