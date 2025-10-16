from app import app
import json

def test_get_users():
    client = app.test_client()
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert "name" in data[0]

def test_add_user():
    client = app.test_client()
    new_user = {"id": 3, "name": "Kumar", "email": "kumar@example.com"}
    response = client.post('/users', data=json.dumps(new_user), content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data["user"]["name"] == "Kumar"
