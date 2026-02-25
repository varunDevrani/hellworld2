from typing import Union, List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User
from src.repositories.interfaces.user_repository import IUserRepository
from src.schemas.user import UserUpdateRequest


class UserRepository(IUserRepository):

	def __init__(self, db: Session):
		self.db = db

	def find_by_email(self, email: str) -> Union[User, None]:
		stmt = select(User).where(User.email == email)
		user_data = self.db.scalar(stmt)
		return user_data
		# return self.db.query(User).filter(User.email == email).first()
	
	def find_by_id(
		self,
		id: UUID
	) -> Union[User, None]:
		stmt = select(User).where(User.id == id)
		user_data = self.db.scalar(stmt)
		return user_data
		
	def find_all(
		self
	) -> List[User]:
		stmt = select(User)
		users_data = self.db.scalars(stmt).all()
		return list(users_data)
			
	def create(self, email: str, password_hash: str) -> User:
		user_data = User(
			email=email,
			password_hash=password_hash
		)
		self.db.add(user_data)
		self.db.commit()
		self.db.refresh(user_data)

		return user_data
		
	def update_by_id(
		self,
		id: UUID,
		payload: UserUpdateRequest
	) -> Union[User, None]:
		
		user_data = self.find_by_id(id)
		if not user_data:
			return None
		
		updated_payload = payload.model_dump(exclude_none=True, exclude_unset=True)
		for key, value in updated_payload.items():
			setattr(user_data, key, value)
			
		self.db.commit()
		self.db.refresh(user_data)
		return user_data
