from typing import List, Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud import crud_task
from databases import get_async_session
from models.task import Task
from schemas import TaskCreate, TaskResponse, TaskUpdate
from security.token import check_authorization
from utilities.exceptions import TaskNotFound

router = APIRouter(dependencies=[Depends(check_authorization)])


@router.get(
    path="/",
    response_model=List[TaskResponse],
    status_code=status.HTTP_200_OK,
    summary="Retrieve all tasks",
    description=(
        "Fetches a list of all tasks stored in the database. "
        "Authorization is required to access this endpoint."
    ),
)
async def read_all_tasks(
    db: AsyncSession = Depends(get_async_session),
):
    """
    Fetch all tasks.

    This endpoint returns all tasks from the database. Authorization is
    required to access the task list.

    Args:
        db (AsyncSession): The asynchronous session for database access.
        authorization (Callable): User authorization validation.

    Returns:
        List[TaskResponse]: A list of all tasks if found or empty list
        if not found.
    """
    return await crud_task.read_all(db)


@router.get(
    path="/{task_id}/",
    status_code=status.HTTP_200_OK,
    response_model=TaskResponse,
    summary="Retrieve a task by ID",
    description=(
        "Returns information about a specific task by its unique ID. "
        "If the task is not found, an error is returned."
    ),
)
async def read_task(
    task_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Fetch a task by ID.

    This endpoint returns the details of a specific task by its ID. If the task
    does not exist, an error will be raised.

    Args:
        task_id (int): The unique identifier of the task.
        db (AsyncSession): The asynchronous session for database access.
        authorization (Callable): User authorization validation.

    Returns:
        TaskResponse: The task data if found.

    Raises:
        TaskNotFound: If the task with the given ID does not exist.
    """
    task: Task = await crud_task.read_by_id(db=db, obj_id=task_id)
    if not task:
        raise TaskNotFound(task_id)
    return task


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskResponse,
    summary="Create a new task",
    description=(
        "Creates a new task in the database. " "Authorization is required."
    ),
)
async def create_task(
    create_data: TaskCreate,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Create a new task.

    This endpoint creates a new task in the database. Authorization is required
    to create a task.

    Args:
        create_data (TaskCreate): The data required to create a new task.
        db (AsyncSession): The asynchronous session for database access.
        authorization (Callable): User authorization validation.

    Returns:
        TaskResponse: The created task data.
    """
    return await crud_task.create(db=db, create_data=create_data)


@router.patch(
    "/{task_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Optional[TaskResponse],
    summary="Update a task by ID",
    description=(
        "Updates an existing task by its unique ID. "
        "If the task is not found, 404 error is returned."
    ),
)
async def update_task(
    task_id: int,
    update_data: TaskUpdate,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Update a task by ID.

    This endpoint updates the details of an existing task by its ID.
    If the task does not exist, an error will be raised.

    Args:
        task_id (int): The unique identifier of the task to be updated.
        update_data (TaskUpdate): The data to update the task with.
        db (AsyncSession): The asynchronous session for database access.
        authorization (Callable): User authorization validation.

    Returns:
        Optional[TaskResponse]: The updated task data if the update was
        successful.

    Raises:
        TaskNotFound: If the task with the given ID does not exist.
    """
    updated_task: Task = await crud_task.update(
        db=db,
        update_data=update_data,
        obj_id=task_id,
    )
    if not updated_task:
        raise TaskNotFound(task_id)
    return updated_task


@router.delete(
    "/{task_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task by ID",
    description=(
        "Deletes an existing task by its unique ID. "
        "If the task is not found, 404 error is returned."
    ),
)
async def remove_task(
    task_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Delete a task by ID.

    This endpoint deletes an existing task from the database by its ID.
    If the task does not exist, 404 error will be raised.

    Args:
        task_id (int): The unique identifier of the task to be deleted.
        db (AsyncSession): The asynchronous session for database access.
        authorization (Callable): User authorization validation.

    Raises:
        TaskNotFound: If the task with the given ID does not exist.
    """
    await crud_task.remove(db=db, obj_id=task_id)
