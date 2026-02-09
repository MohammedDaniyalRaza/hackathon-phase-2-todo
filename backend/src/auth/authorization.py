from fastapi import HTTPException, status
from sqlmodel import Session
from src.models.user import User
from src.models.task import Task

def check_user_owns_task(session: Session, user_id: str, task_id: str) -> bool:
    """
    Check if a user owns a specific task
    """
    task = session.get(Task, task_id)
    if not task:
        return False
    return str(task.user_id) == user_id

def check_user_exists(session: Session, user_id: str) -> bool:
    """
    Check if a user exists
    """
    user = session.get(User, user_id)
    return user is not None

def authorize_user_for_task(session: Session, user_id: str, task_id: str):
    """
    Authorize that a user can access a specific task
    Raises HTTPException if not authorized
    """
    if not check_user_exists(session, user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if not check_user_owns_task(session, user_id, task_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this task"
        )