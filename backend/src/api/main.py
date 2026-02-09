from fastapi import APIRouter
from src.api import auth, tasks, refresh

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(refresh.router, prefix="/auth", tags=["auth"])