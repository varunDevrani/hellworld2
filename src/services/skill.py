from uuid import UUID
from typing import List, Dict, Any

from src.repositories.interfaces.skill_repository import ISkillRepository
from src.repositories.interfaces.skill_activity_repository import ISkillActivityRepository
from src.exceptions import AuthenticationError

def get_skills(
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
) -> List[Dict[str, Any]]:
	
	if user_id is None:
		raise AuthenticationError("invalid token")

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