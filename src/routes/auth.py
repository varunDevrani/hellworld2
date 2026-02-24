from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from src.dependencies.database import get_db
from src.schemas.auth import SignupRequest, LoginRequest, RefreshTokenRequest
import src.controllers.auth as controllers

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup")
def signup(
    request: Request,
    response: Response,
    payload: SignupRequest,
    db: Session = Depends(get_db)
):
    return controllers.signup(
        request,
        response,
        payload,
        db
	)
    

@router.post("/login")
def login(
    request: Request,
    response: Response,
    payload: LoginRequest,
    db: Session = Depends(get_db)
):
    return controllers.login(
        request,
        response,
        payload,
        db
	)


@router.post("/refresh")
def refresh(
    request: Request,
    response: Response,
    payload: RefreshTokenRequest,
    db: Session = Depends(get_db)
):
    return controllers.refresh(
        request,
        response,
        payload,
        db
	)


@router.post("/logout")
def logout(
    request: Request,
    response: Response,
    payload: RefreshTokenRequest,
    db: Session = Depends(get_db)
):
    return controllers.logout(
        request,
        response,
        payload,
        db
	)

