import uuid

from datetime import datetime, timezone
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base

class RefreshToken(Base):
	__tablename__ = "refresh_tokens"

	id: Mapped[uuid.UUID] = mapped_column(
		UUID(as_uuid=True),
		primary_key=True,
		default=uuid.uuid4
	)

	user_id: Mapped[UUID] = mapped_column(
		ForeignKey("users.id")
	)

	token: Mapped[str] = mapped_column()

	issued_at: Mapped[datetime] = mapped_column()

	expires_at: Mapped[datetime] = mapped_column()

	created_at: Mapped[datetime] = mapped_column(
		default=lambda: datetime.now(timezone.utc)
	)