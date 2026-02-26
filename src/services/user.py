from uuid import UUID
from typing import List

from src.models.user import User
from src.repositories.interfaces.user_repository import IUserRepository
from src.exceptions import DomainException, ErrorCode, ErrorDetail, FieldViolation
from src.schemas.user import UserUpdateRequest


def get_users(
    user_repo: IUserRepository
) -> List[User]:
    users_data = user_repo.find_all()
    return users_data


def get_user_by_id(
    user_id: UUID,
    user_repo: IUserRepository
) -> User:
					
	user_data = user_repo.find_by_id(user_id)
	if not user_data:
		raise DomainException(
			404,
			ErrorCode.NOT_FOUND_ERROR,
			"user_id not found",
			ErrorDetail(
				resource="users",
				field_violations=[
					FieldViolation(
						field="user_id"
					)
				]
			)
		)
	
	return user_data


def update_user_by_id(
	payload: UserUpdateRequest,
	user_id: UUID,
	user_repo: IUserRepository
) -> User:
		
	user_data = user_repo.update_by_id(user_id, payload)
	if user_data is None:
		raise DomainException(
			404,
			ErrorCode.NOT_FOUND_ERROR,
			"user_id not found",
			ErrorDetail(
				resource="users",
				field_violations=[
					FieldViolation(
						field="user_id"
					)
				]
			)
		)

	return user_data
	