

class DomainException(Exception):
	def __init__(self, message: str):
		self.message = message
		super().__init__(message)


class ConflictError(DomainException):
	pass

class ValidationError(DomainException):
	pass

class AuthenticationError(DomainException):
	pass

class InvalidRefreshTokenError(DomainException):
	pass

class NotFoundError(DomainException):
	def __init__(self, resource: str):
		self.resource = resource
		super().__init__(f"{resource} not found")

