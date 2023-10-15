```python
import unittest
import json
from api import app

class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_tasks(self):
        response = self.app.get('/api/tasks')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_post_task(self):
        response = self.app.post('/api/task', data=json.dumps(dict(url='http://example.com')), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_task(self):
        response = self.app.get('/api/task/1')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_delete_task(self):
        response = self.app.delete('/api/task/1')
        self.assertEqual(response.status_code, 204)

    def test_get_logs(self):
        response = self.app.get('/api/logs')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
```