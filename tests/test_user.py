import unittest
from models.user import User

class TestUser(unittest.TestUser):
    def test_user_initialization(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes(self):
        user = User(email = "test@example.com" password = "password", first_name = "John", last_name = "Doe")
        self.assertEqual(user.email, "test@exammple.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
