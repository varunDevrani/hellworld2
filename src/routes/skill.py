from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from src.dependencies.database import get_db
from src.schemas.skill import SkillCreateRequest, SkillUpdateRequest
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
):
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
):
    pass
    
  
@router.delete("/{skill_id}")
def delete_skill_by_id(
    request: Request,
    response: Response,
    skill_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass


@router.patch("/{skill_id}")
def update_skill_by_id(
    request: Request,
    response: Response,
    payload: SkillUpdateRequest,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass


@router.get("/{skill_id}")
@router.get("/{skill_id}/activities")
def get_skill_by_id(
    request: Request,
    response: Response,
    skill_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass
    
@router.post("/{skill_id}/activities")
def create_skill_activity(
	request: Request,
	response: Response,
	db: Session = Depends(get_db),
	user_id: UUID = Depends(get_current_user)
):
	pass


@router.get("/{skill_id}/activities/{activity_id}")
def get_skill_activity_by_id(
    request: Request,
    response: Response,
    activity_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass
    

@router.delete("/{skill_id}/activities/{activity_id}")
def delete_skill_activity_by_id(
    request: Request,
    response: Response,
    activity_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass


@router.patch("/{skill_id}/activities/{activity_id}")
def update_skill_activity_by_id(
	request: Request,
	response: Response,
	activity_id: UUID,
	db: Session = Depends(get_db),
	user_id: UUID = Depends(get_current_user)
):
	pass

