from crud.base import CRUDBase
from models.task import Task


class CRUDTask(CRUDBase):
    """
    A specific CRUD class for managing Task objects.

    This class inherits from CRUDBase and provides an interface for performing
    CRUD operations specifically on Task instances in the database.

    Inherits:
        CRUDBase: A generic CRUD class for managing SQLAlchemy models.
    """

    ...


crud_task = CRUDTask(Task)
"""
An instance of CRUDTask for managing Task objects.

This instance can be used to perform create, read, update, and delete
operations on Task instances in the database.
"""
