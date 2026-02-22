from typing import Union
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User
from src.repositories.interfaces.user_repository import IUserRepository


class UserRepository(IUserRepository):

	def __init__(self, db: Session):
		self.db = db

	def find_by_email(self, email: str) -> Union[User, None]:
		stmt = select(User).where(User.email == email)
		user_data = self.db.scalar(stmt)
		return user_data
		# return self.db.query(User).filter(User.email == email).first()
			
	def create(self, email: str, password_hash: str) -> User:
		user_data = User(
			email=email,
			password_hash=password_hash
		)
		self.db.add(user_data)
		self.db.commit()
		self.db.refresh(user_data)

		return user_data
