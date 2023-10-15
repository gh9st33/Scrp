```python
import unittest
from webapp.user_auth import UserAuth

class TestUserAuth(unittest.TestCase):

    def setUp(self):
        self.user_auth = UserAuth()

    def test_register_user(self):
        response = self.user_auth.register_user('testuser', 'testpassword')
        self.assertEqual(response['status'], 'success')

    def test_login_user(self):
        self.user_auth.register_user('testuser', 'testpassword')
        response = self.user_auth.login_user('testuser', 'testpassword')
        self.assertEqual(response['status'], 'success')

    def test_invalid_login(self):
        response = self.user_auth.login_user('invaliduser', 'invalidpassword')
        self.assertEqual(response['status'], 'failure')

    def test_duplicate_register(self):
        self.user_auth.register_user('testuser', 'testpassword')
        response = self.user_auth.register_user('testuser', 'testpassword')
        self.assertEqual(response['status'], 'failure')

if __name__ == '__main__':
    unittest.main()
```