import pytest
from fastapi.testclient import TestClient
from src.main import app
from sqlmodel import SQLModel, create_engine
from src.database import engine
from unittest.mock import patch

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Todo API"}

@patch('src.services.user_service.get_user_by_email')
def test_login_nonexistent_user(mock_get_user):
    mock_get_user.return_value = None
    response = client.post("/v1/auth/login", json={"email": "nonexistent@example.com", "password": "password"})
    assert response.status_code == 401

@patch('src.services.user_service.create_user')
@patch('src.services.user_service.get_user_by_email')
def test_register_user(mock_get_user, mock_create_user):
    # Mock that user doesn't exist yet
    mock_get_user.return_value = None
    # Mock user creation
    mock_create_user.return_value = {"id": 1, "email": "test@example.com", "is_active": True}
    
    response = client.post("/v1/auth/register", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200