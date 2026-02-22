from typing import Union
from abc import ABC, abstractmethod

from src.models.user import User


class IUserRepository(ABC):

	@abstractmethod
	def find_by_email(
		self, 
		email: str
	) -> Union[User, None]:
		
		raise NotImplementedError
	
	@abstractmethod
	def create(
		self, 
		email: str, 
		password_hash: str
	) -> User:
		
		raise NotImplementedError
