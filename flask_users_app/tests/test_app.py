import unittest  # Stdlib

from app import app  # Local


class TestFlaskUsersApp(unittest.TestCase):
    """Unit tests for Flask users app."""

    def setUp(self):
        self.client = app.test_client()

    def test_add_user(self):
        response = self.client.get("/users/add/John")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"name": "John"})

    def test_get_users(self):
        self.client.get("/users/add/John")
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"users": ["John"]})


if __name__ == "__main__":
    unittest.main()
