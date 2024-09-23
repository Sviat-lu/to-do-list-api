from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Task(Base):
    """
    Represents the 'task' table in the database, used to store task-related
    information.

    Attributes:
        - id (int): The primary key of the task.
        - created_at (datetime): The timestamp when the task was created, set
        to the current time by default.
        - updated_at (datetime): The timestamp when the task was last updated,
        automatically set when the task is updated.
        - date_to_do (datetime): The specific date and time the task is
        scheduled to be done.
        - task_info (str): A text field containing information about the task.
    """

    __tablename__ = "task"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_onupdate=func.now()
    )
    date_to_do: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    task_info: Mapped[str] = mapped_column(String(length=255))
