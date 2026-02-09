from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Any
from src.database import engine
from src.models.user import User, UserCreate, UserRead
from src.services.user_service import get_user_by_email, create_user
from src.utils.password import verify_password
from src.utils.jwt import create_access_token
from datetime import timedelta
from src.utils.jwt import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/register", response_model=UserRead)
def register_user(user_create: UserCreate):
    with Session(engine) as session:
        # Check if user already exists
        existing_user = get_user_by_email(session=session, email=user_create.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )
        
        # Create new user
        user = create_user(session=session, user_create=user_create)
        return user

@router.post("/login")
def login_user(user_credentials: UserCreate):
    with Session(engine) as session:
        # Get user by email
        user = get_user_by_email(session=session, email=user_credentials.email)
        if not user or not verify_password(user_credentials.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
        
        # Create access token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
def logout_user():
    # In a stateless JWT system, the server doesn't store session info
    # So logout is typically handled on the client side by removing the token
    return {"message": "Logged out successfully"}