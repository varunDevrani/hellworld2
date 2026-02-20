from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.connect_db import get_db
from src.schemas.skills import SkillCreateRequest, SkillUpdateRequest
from src.utils.get_current_user import get_current_user


router = APIRouter(
    prefix="/skills",
    tags=["skills"]
)


@router.get("/")
def get_skills(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass


@router.get("/{skill_id}")
def get_skills_by_id(
    request: Request,
    response: Response,
    skill_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass
    

@router.get("/{activity_id}")
def get_skill_activity_by_id(
    request: Request,
    response: Response,
    activity_id: UUID,
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


@router.delete("/{activity_id}")
def delete_skill_activity_by_id(
    request: Request,
    response: Response,
    activity_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass


@router.post("/")
def create_skill(
    request: Request,
    response: Response,
    payload: SkillCreateRequest,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass
    

@router.put("/{skill_id}")
@router.patch("/{skill_id}")
def update_skill_by_id(
    request: Request,
    response: Response,
    payload: SkillUpdateRequest,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass

