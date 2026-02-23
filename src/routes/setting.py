from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.connect_db import get_db
from src.schemas.setting import GeneralSettingsUpdateRequest, NotificationSettingsUpdateRequest
from src.dependencies.get_current_user import get_current_user


router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("/general")
def get_settings_general(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass


@router.patch("/general")
def update_settings_general(
    request: Request,
    response: Response,
    payload: GeneralSettingsUpdateRequest,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass


@router.get("/notifications")
def get_settings_notifications(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass
    
    
@router.patch("/notifications")
def update_settings_notifications(
    request: Request,
    response: Response,
    payload: NotificationSettingsUpdateRequest,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
):
    pass

