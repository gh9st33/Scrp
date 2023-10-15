```python
import unittest
from flask import Flask
from flask_login import LoginManager
from web_app.user_auth import UserAuth

class TestUserAuth(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.login_manager = LoginManager(self.app)
        self.user_auth = UserAuth(self.login_manager)

    def test_login(self):
        test_user = {"username": "test", "password": "test123"}
        result = self.user_auth.login(test_user)
        self.assertEqual(result, True)

    def test_logout(self):
        result = self.user_auth.logout()
        self.assertEqual(result, True)

    def test_register(self):
        test_user = {"username": "test", "password": "test123"}
        result = self.user_auth.register(test_user)
        self.assertEqual(result, True)

    def test_load_user(self):
        test_user_id = 1
        result = self.user_auth.load_user(test_user_id)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
```