from app import app

def test_home():
    # Flask provides a test client for unit tests
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World! Welcome to Flask backend."}
