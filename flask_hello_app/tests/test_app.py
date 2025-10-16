import unittest  # Stdlib

from app import app  # Local


class TestHelloApp(unittest.TestCase):
    """Unit tests for Flask hello app."""

    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"message": "Hello, World! Welcome to Flask backend."},
        )


if __name__ == "__main__":
    unittest.main()
