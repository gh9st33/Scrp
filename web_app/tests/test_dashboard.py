```python
import unittest
from flask import url_for
from web_app.server import app

class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_dashboard_status_code(self):
        response = self.app.get(url_for('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_data(self):
        response = self.app.get(url_for('dashboard'))
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('active_tasks', data)
        self.assertIn('completed_tasks', data)

    def test_dashboard_active_tasks(self):
        response = self.app.get(url_for('dashboard'))
        data = response.get_json()
        active_tasks = data['active_tasks']
        self.assertIsInstance(active_tasks, list)

    def test_dashboard_completed_tasks(self):
        response = self.app.get(url_for('dashboard'))
        data = response.get_json()
        completed_tasks = data['completed_tasks']
        self.assertIsInstance(completed_tasks, list)

if __name__ == "__main__":
    unittest.main()
```