from sqlmodel import Session, select
from src.models.task import Task, TaskCreate, TaskUpdate
from typing import List, Optional
from uuid import UUID

def create_task(*, session: Session, task_create: TaskCreate, user_id: UUID) -> Task:
    db_task = Task.from_orm(task_create)
    db_task.user_id = user_id
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

def get_tasks_by_user(*, session: Session, user_id: UUID) -> List[Task]:
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    return tasks

def get_task_by_id(*, session: Session, task_id: UUID, user_id: UUID) -> Optional[Task]:
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = session.exec(statement).first()
    return task

def update_task(*, session: Session, task_id: UUID, task_update: TaskUpdate, user_id: UUID) -> Optional[Task]:
    db_task = get_task_by_id(session=session, task_id=task_id, user_id=user_id)
    if not db_task:
        return None
        
    task_data = task_update.dict(exclude_unset=True)
    for field, value in task_data.items():
        setattr(db_task, field, value)
    
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

def delete_task(*, session: Session, task_id: UUID, user_id: UUID) -> bool:
    db_task = get_task_by_id(session=session, task_id=task_id, user_id=user_id)
    if not db_task:
        return False
    
    session.delete(db_task)
    session.commit()
    return True