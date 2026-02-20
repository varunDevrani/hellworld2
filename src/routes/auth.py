from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from src.database.connect_db import get_db
from src.schemas.auth import SignupRequest, LoginRequest


router = APIRouter(prefix="/api/v1", tags=["auth"])


@router.post("/signup")
def signup(
    request: Request,
    response: Response,
    payload: SignupRequest,
    db: Session = Depends(get_db)
):
    pass
    

@router.post("/login")
def login(
    request: Request,
    response: Response,
    payload: LoginRequest,
    db: Session = Depends(get_db)
):
    pass