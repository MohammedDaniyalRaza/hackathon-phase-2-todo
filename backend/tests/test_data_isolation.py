import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.pool import StaticPool
from unittest.mock import patch

from src.main import app
from src.database import engine
from src.models.user import User
from src.models.task import Task

client = TestClient(app)

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", 
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    SQLModel.metadata.create_all(bind=engine)
    with Session(engine) as session:
        yield session

def test_data_isolation_between_users(session):
    """
    Test that users can only access their own tasks
    """
    # Create two users
    user1_data = {"email": "user1@example.com", "password": "password123"}
    user2_data = {"email": "user2@example.com", "password": "password123"}
    
    # Register both users
    response1 = client.post("/v1/auth/register", json=user1_data)
    response2 = client.post("/v1/auth/register", json=user2_data)
    
    assert response1.status_code == 200
    assert response2.status_code == 200
    
    # Login as user1 and get token
    login_response1 = client.post("/v1/auth/login", json=user1_data)
    assert login_response1.status_code == 200
    token1 = login_response1.json()["access_token"]
    
    # Login as user2 and get token
    login_response2 = client.post("/v1/auth/login", json=user2_data)
    assert login_response2.status_code == 200
    token2 = login_response2.json()["access_token"]
    
    # Create a task for user1
    task_data = {"title": "User1's task", "description": "A task for user1"}
    headers1 = {"Authorization": f"Bearer {token1}"}
    create_task_response = client.post("/v1/tasks", json=task_data, headers=headers1)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["id"]
    
    # Verify user1 can access their own task
    get_task_response = client.get(f"/v1/tasks/{task_id}", headers=headers1)
    assert get_task_response.status_code == 200
    assert get_task_response.json()["id"] == task_id
    
    # Verify user2 cannot access user1's task
    headers2 = {"Authorization": f"Bearer {token2}"}
    get_task_response_user2 = client.get(f"/v1/tasks/{task_id}", headers=headers2)
    assert get_task_response_user2.status_code == 404  # Task not found for user2
    
    # Verify user2 can only see their own (empty) list of tasks
    get_tasks_response_user2 = client.get("/v1/tasks", headers=headers2)
    assert get_tasks_response_user2.status_code == 200
    assert len(get_tasks_response_user2.json()) == 0  # User2 has no tasks
    
    # Verify user1 can still see their task
    get_tasks_response_user1 = client.get("/v1/tasks", headers=headers1)
    assert get_tasks_response_user1.status_code == 200
    assert len(get_tasks_response_user1.json()) == 1
    assert get_tasks_response_user1.json()[0]["id"] == task_id