
import unittest

def login(username, password):
    if username == "student" and password == "12345":
        return "Login successful"
    return "Invalid credentials"

class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        self.assertEqual(
            login("student", "12345"),
            "Login successful"
        )

    def test_invalid_login(self):
        self.assertEqual(
            login("student", "wrong"),
            "Invalid credentials"
        )

    def test_empty_username(self):
        self.assertEqual(
            login("", "12345"),
            "Invalid credentials"
        )

if __name__ == "__main__":
    unittest.main()
