from fastapi import Request, Response
from fastapi.responses import JSONResponse
from uuid import UUID
from sqlalchemy.orm import Session

from src.repositories.skill_repository import SkillRepository
from src.repositories.skill_activity_repository import SkillActivityRepository
from src.schemas.api_response import SuccessResponse
from src.schemas.skill import SkillActivityCreateRequest, SkillCreateRequest, SkillUpdateRequest, SkillsResponse
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

	return SuccessResponse(
		status_code=200,
		message="Skills[user_id] fetched successfully.",
		data={
			"skills": SkillsResponse.model_validate({
				"total_skills": len(all_skills_data),
				"skills": all_skills_data
			}).model_dump(mode="json")
		}
	)


def create_skill(
	request: Request,
	response: Response,
	payload: SkillCreateRequest,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	pass
	

def delete_skill_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	pass


def update_skill_by_id(
	request: Request,
	response: Response,
	payload: SkillUpdateRequest,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	pass


def get_skill_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	pass


def create_skill_activity(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillActivityCreateRequest,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	pass


def get_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	pass


def delete_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	pass


def update_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	db: Session,
	user_id: UUID
) -> JSONResponse:
	pass

