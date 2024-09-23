from fastapi import HTTPException, status


class ObjectNotFound(HTTPException):
    """
    Custom exception for handling cases when any object is not found.
    This exception is raised when a requested object cannot be located in the
    database. It inherits from HTTPException and provides a specific detail
    message and HTTP status code.

    Attributes:
        - detail (str): A message describing the error (default: "{Object} with
        ID {id} not found").
        - status_code (int): The HTTP status code associated with the error
        (default: 404 Not Found).
    """

    def __init__(self, object_name: str = "Object", object_id: int = None):
        detail = (
            f"{object_name} with ID {object_id} not found"
            if object_id
            else f"{object_name} not found"
        )
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class TaskNotFound(ObjectNotFound):
    """
    Custom exception for handling cases when a task is not found.
    This exception is raised when a requested task cannot be located in the
    database. Inherits from ObjectNotFound and sets a specific message
    for tasks.
    """

    def __init__(self, task_id: int = None):
        super().__init__(object_name="Task", object_id=task_id)
