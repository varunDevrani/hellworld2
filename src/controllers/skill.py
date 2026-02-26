from fastapi import Request, Response
from fastapi.responses import JSONResponse
from uuid import UUID
from sqlalchemy.orm import Session

from src.repositories.skill_repository import SkillRepository
from src.repositories.skill_activity_repository import SkillActivityRepository
import src.services.skill as services


def get_skills(
	request: Request,
	response: Response,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	
	skill_repo = SkillRepository(db)
	skill_activity_repo = SkillActivityRepository(db)

	all_skills_data = services.get_skills(
		user_id,
		skill_repo,
		skill_activity_repo
	)

	response.status_code = 200
	return JSONResponse(
		status_code=200,
		content={
			"success": True,
			"data": {
				"skills": all_skills_data
			}
		}
	)

