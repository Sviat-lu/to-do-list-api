from fastapi import APIRouter

from .endpoints import auth_router, tasks_router

api_v1_router = APIRouter(prefix="/v1")


api_v1_router.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])
api_v1_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
