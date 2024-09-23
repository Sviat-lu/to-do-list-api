from datetime import datetime
from typing import Optional

from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, model_validator


class TaskBase(BaseModel):
    """
    Base model for task-related data. This model contains the common attributes
    that are shared between different task operations such as creating,
    updating, and retrieving tasks.

    Attributes:
        - date_to_do (datetime): The date and time when the task is scheduled
        to be done.
        - task_info (str): A string containing additional information or
        description about the task.
    """

    date_to_do: datetime
    task_info: str


class TaskResponse(TaskBase):
    """
    Response model for a task. This model inherits from TaskBase and is used
    to return task data from the API, such as when retrieving a task or
    listing tasks.

    Inherits:
        TaskBase: The base task attributes (date_to_do, task_info).
    """

    ...


class TaskCreate(TaskBase):
    """
    Model for creating a new task. This model is used when a client sends
    data to the API to create a new task in the system.

    Inherits:
        TaskBase: The base task attributes (date_to_do, task_info) that
        are required for creating a task.
    """

    ...


class TaskUpdate(TaskBase):
    """
    Model for updating an existing task. This model allows partial updates to
    the task's fields, meaning both `date_to_do` and `task_info` are optional.
    If provided, they will overwrite the existing data.

    Attributes:
        - date_to_do (Optional[datetime]): The updated date and time for the
        task (optional).
        task_info (Optional[str]): The updated task information (optional).

    Inherits:
        TaskBase: The base task attributes, though they are optional for
        updates.

    Raises:
        RequestValidationError: If neither `date_to_do` nor `task_info` is
        provided for the update.
    """

    date_to_do: Optional[datetime] = None
    task_info: Optional[str] = None

    @model_validator(mode="after")
    def check_fields(self):
        """
        Validates that at least one field (`date_to_do` or `task_info`) is
        provided when updating a task. If neither field is provided, it raises
        a validation error.

        Raises:
            RequestValidationError: If both `date_to_do` and `task_info`
            are None.

        Example:
            If a user tries to update a task without specifying any fields to
            change, this validation will trigger to ensure that at least one
            field is being updated.
        """
        if not self.date_to_do and not self.task_info:
            raise RequestValidationError(
                "Please specify at least one field to change."
            )
        return self
