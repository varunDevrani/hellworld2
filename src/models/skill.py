import uuid
from datetime import datetime, timezone
from typing import Union
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class Skill(Base):
	__tablename__ = "skills"
    
	id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
	)
    
	user_id: Mapped[uuid.UUID] = mapped_column(
		ForeignKey("users.id")
	)

	name: Mapped[str] = mapped_column()

	created_at: Mapped[datetime] = mapped_column(
		default=lambda: datetime.now(timezone.utc)
	)

	updated_at: Mapped[datetime] = mapped_column(
		default=lambda: datetime.now(timezone.utc),
		onupdate=lambda: datetime.now(timezone.utc)
	)

	deleted_at: Mapped[Union[datetime, None]] = mapped_column()

