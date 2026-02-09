from sqlmodel import Session, select
from src.models.user import User, UserCreate
from src.utils.password import hash_password
from typing import Optional

def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_user = User.from_orm(user_create)
    db_user.password_hash = hash_password(user_create.password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_user_by_email(*, session: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    return user

def get_user_by_id(*, session: Session, user_id: str) -> Optional[User]:
    statement = select(User).where(User.id == user_id)
    user = session.exec(statement).first()
    return user