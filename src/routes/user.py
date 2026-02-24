from uuid import UUID
from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.dependencies.database import get_db
import src.controllers.user as controllers

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
def get_users(
    request: Request,
    response: Response,
    db: Session = Depends(get_db)
) -> JSONResponse:
    return controllers.get_users(
        request,
        response,
        db
    )


@router.get("/{user_id}")
def get_user_by_id(
    request: Request,
    response: Response,
    user_id: UUID,
    db: Session = Depends(get_db),
) -> JSONResponse:
    return controllers.get_user_by_id(
        request,
        response,
        user_id,
        db
    )
    
