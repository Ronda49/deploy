import unittest  # Stdlib

from fastapi.testclient import TestClient  # Third-party

from main import app  # Local


class TestFastAPITodoApp(unittest.TestCase):
    """Unit tests for FastAPI Todo app."""

    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"message": "Welcome to FastAPI Todo app"}
        )

    def test_create_todo(self):
        response = self.client.post("/todo/", json="Test task")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item": "Test task"})


if __name__ == "__main__":
    unittest.main()
