from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base
from core.base.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from domains.tags import Tags
    from domains.users import User


class Queue(IntIdPkMixin, Base):
    __tablename__ = "queues"

    name: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )
    start_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )
    max_slots: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=30,
    )

    # по названию связи в связуемой таблице
    entries: Mapped[List["QueueEntries"]] = relationship(
        "QueueEntries",
        back_populates="queue",
    )
    queue_tags: Mapped[List["Tags"]] = relationship(
        "Tags",
        secondary="queue_tags",
        back_populates="queues",
    )

    __table_args__ = (
        CheckConstraint(
            "max_slots BETWEEN 1 AND 40",
            name="check_position_number",
        ),
        CheckConstraint(
            "start_time >= CURRENT_DATE",
            name="check_event_date",
        ),
    )


class QueueEntries(IntIdPkMixin, Base):
    __tablename__ = "queue_entries"

    queue_id: Mapped[int] = mapped_column(
        ForeignKey(
            "queues.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )
    user_id: Mapped[str] = mapped_column(
        ForeignKey(
            "user.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )
    position: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    queue: Mapped[Queue] = relationship(
        "Queue",
        back_populates="entries",
    )
    user: Mapped["User"] = relationship(
        "User",
        back_populates="queue_entries",
    )

    __table_args__ = (
        UniqueConstraint(
            "queue_id",
            "position",
            name="uq_queue_position",
        ),
        UniqueConstraint(
            "queue_id",
            "user_id",
            name="uq_queue_user",
        ),
        CheckConstraint(
            "position BETWEEN 1 AND 30",
            name="check_position_range",
        ),
    )


class QueueTags(IntIdPkMixin, Base):
    __tablename__ = "queue_tags"

    queue_id: Mapped[int] = mapped_column(
        ForeignKey(
            "queues.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    tag_id: Mapped[int] = mapped_column(
        ForeignKey(
            "tags.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            "queue_id",
            "tag_id",
            name="uq_username_email",
        ),
    )
