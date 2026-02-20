from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.connect_db import get_db
from src.utils.get_current_user import get_current_user


router = APIRouter(
    prefix="/skills",
    tags=["skills"]
)

