import uuid
import datetime
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base

class SkillActivity(Base):
	__tablename__ = "skill_activities"

	id: Mapped[uuid.UUID] = mapped_column(
		UUID(as_uuid=True),
		primary_key=True,
		default=uuid.uuid4
	)

	skill_id: Mapped[uuid.UUID] = mapped_column(
		ForeignKey("skills.id")
	)

	date: Mapped[datetime.date] = mapped_column(
		default=datetime.date.today
	)

	name: Mapped[str] = mapped_column()

	is_completed: Mapped[bool] = mapped_column(
		default=False
	)

	is_priority: Mapped[bool] = mapped_column(
		default=False
	)

	is_habit_to_protect: Mapped[bool] = mapped_column(
		default=False
	)

	minutes_practised: Mapped[int] = mapped_column(
		default=0
	)

	created_at: Mapped[datetime.datetime] = mapped_column(
		default=lambda: datetime.datetime.now(datetime.timezone.utc)
	)

	updated_at: Mapped[datetime.datetime] = mapped_column(
		default=lambda: datetime.datetime.now(datetime.timezone.utc),
		onupdate=lambda: datetime.datetime.now(datetime.timezone.utc)
	)

