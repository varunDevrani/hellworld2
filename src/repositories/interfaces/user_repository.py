from typing import Union, List
from abc import ABC, abstractmethod
from uuid import UUID

from src.models.user import User


class IUserRepository(ABC):

	@abstractmethod
	def find_by_email(
		self, 
		email: str
	) -> Union[User, None]:
		raise NotImplementedError
		
	@abstractmethod
	def find_by_id(
		self,
		id: UUID
	) -> Union[User, None]:
		raise NotImplementedError
		
	@abstractmethod
	def find_all(
		self
	) -> List[User]:
		raise NotImplementedError
	
	@abstractmethod
	def create(
		self, 
		email: str, 
		password_hash: str
	) -> User:
		raise NotImplementedError
