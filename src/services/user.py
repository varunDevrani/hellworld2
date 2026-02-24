from uuid import UUID
from typing import List

from src.models.user import User
from src.repositories.interfaces.user_repository import IUserRepository
from src.exceptions import NotFoundError


def get_users(
    user_repo: IUserRepository
) -> List[User]:
    users_data = user_repo.find_all()
    return users_data


def get_user_by_id(
    user_id: UUID,
    user_repo: IUserRepository
) -> User:
	if not user_id:
		raise NotFoundError("user")
					
	user_data = user_repo.find_by_id(user_id)
	if not user_data:
		raise NotFoundError("user")
	
	return user_data
