from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlmodel import Session
from typing import List
from uuid import UUID
from src.database import engine
from src.models.task import Task, TaskCreate, TaskRead, TaskUpdate
from src.services.task_service import (
    create_task, get_tasks_by_user, get_task_by_id, 
    update_task, delete_task
)
from src.utils.jwt import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user_id = verify_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user_id

@router.get("/", response_model=List[TaskRead])
def read_tasks(current_user_id: str = Depends(get_current_user_id)):
    with Session(engine) as session:
        tasks = get_tasks_by_user(session=session, user_id=UUID(current_user_id))
        return tasks

@router.post("/", response_model=TaskRead)
def create_new_task(task_create: TaskCreate, current_user_id: str = Depends(get_current_user_id)):
    with Session(engine) as session:
        task = create_task(
            session=session, 
            task_create=task_create, 
            user_id=UUID(current_user_id)
        )
        return task

@router.get("/{task_id}", response_model=TaskRead)
def read_task(
    task_id: UUID = Path(..., title="The ID of the task"),
    current_user_id: str = Depends(get_current_user_id)
):
    with Session(engine) as session:
        task = get_task_by_id(
            session=session, 
            task_id=task_id, 
            user_id=UUID(current_user_id)
        )
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        return task

@router.put("/{task_id}", response_model=TaskRead)
def update_existing_task(
    task_update: TaskUpdate,
    task_id: UUID = Path(..., title="The ID of the task"),
    current_user_id: str = Depends(get_current_user_id)
):
    with Session(engine) as session:
        task = update_task(
            session=session,
            task_id=task_id,
            task_update=task_update,
            user_id=UUID(current_user_id)
        )
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        return task

@router.delete("/{task_id}")
def delete_existing_task(
    task_id: UUID = Path(..., title="The ID of the task"),
    current_user_id: str = Depends(get_current_user_id)
):
    with Session(engine) as session:
        success = delete_task(
            session=session,
            task_id=task_id,
            user_id=UUID(current_user_id)
        )
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        return {"message": "Task deleted successfully"}