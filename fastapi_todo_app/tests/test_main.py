from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Todo App"}

def test_add_and_get_todo():
    # Add a todo
    response = client.post("/todos", params={"item": "Buy milk"})
    assert response.status_code == 200
    assert "Added" in response.json()["message"]

    # Get todos
    response = client.get("/todos")
    data = response.json()
    assert "todos" in data
    assert "Buy milk" in data["todos"]
