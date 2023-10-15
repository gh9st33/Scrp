```python
import unittest
from server import app

class TestServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_auth_status_code(self):
        response = self.app.get('/auth')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_status_code(self):
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_deploy_scrapers_status_code(self):
        response = self.app.get('/deploy')
        self.assertEqual(response.status_code, 200)

    def test_data_view_status_code(self):
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)

    def test_logs_metrics_status_code(self):
        response = self.app.get('/logs')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```