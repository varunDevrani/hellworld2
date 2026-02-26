from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from uuid import UUID

from src.dependencies.database import get_db
from src.schemas.skill import SkillActivityCreateRequest, SkillCreateRequest, SkillUpdateRequest
from src.dependencies.auth import get_current_user
import src.controllers.skill as controllers

router = APIRouter(
    prefix="/skills",
    tags=["skills"]
)


@router.get("")
def get_skills(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
    return controllers.get_skills(
        request,
        response,
        db,
        user_id
	)


@router.post("")
def create_skill(
    request: Request,
    response: Response,
    payload: SkillCreateRequest,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.create_skill(
		request,
		response,
		payload,
		db,
		user_id
	)
    
  
@router.delete("/{skill_id}")
def delete_skill_by_id(
    request: Request,
    response: Response,
    skill_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.delete_skill_by_id(
		request,
		response,
		skill_id,
		db,
		user_id
	)


@router.patch("/{skill_id}")
def update_skill_by_id(
    request: Request,
    response: Response,
    payload: SkillUpdateRequest,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.update_skill_by_id(
		request,
		response,
		payload,
		db,
		user_id
	)


@router.get("/{skill_id}")
@router.get("/{skill_id}/activities")
def get_skill_by_id(
    request: Request,
    response: Response,
    skill_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.get_skill_by_id(
		request,
		response,
		skill_id,
		db,
		user_id
	)
    
@router.post("/{skill_id}/activities")
def create_skill_activity(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillActivityCreateRequest,
	db: Session = Depends(get_db),
	user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.create_skill_activity(
		request,
		response,
		skill_id,
		payload,
		db,
		user_id
	)


@router.get("/{skill_id}/activities/{activity_id}")
def get_skill_activity_by_id(
    request: Request,
    response: Response,
    skill_id: UUID,
    activity_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.get_skill_activity_by_id(
		request,
		response,
		skill_id,
		activity_id,
		db,
		user_id
	)
    

@router.delete("/{skill_id}/activities/{activity_id}")
def delete_skill_activity_by_id(
    request: Request,
    response: Response,
    skill_id: UUID,
    activity_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.delete_skill_activity_by_id(
		request,
		response,
		skill_id,
		activity_id,
		db,
		user_id
	)


@router.patch("/{skill_id}/activities/{activity_id}")
def update_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	db: Session = Depends(get_db),
	user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.update_skill_activity_by_id(
		request,
		response,
		skill_id,
		activity_id,
		db,
		user_id
	)

