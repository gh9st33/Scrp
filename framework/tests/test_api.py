```python
import unittest
import json
from flask import Flask
from framework.api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_tasks(self):
        response = self.app.get('/api/tasks')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_post_task(self):
        task = {
            'name': 'test_scraper',
            'url': 'http://test.com',
            'type': 'data'
        }
        response = self.app.post('/api/tasks', data=json.dumps(task), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_task(self):
        response = self.app.get('/api/tasks/1')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_update_task(self):
        task = {
            'name': 'updated_test_scraper',
            'url': 'http://updated-test.com',
            'type': 'image'
        }
        response = self.app.put('/api/tasks/1', data=json.dumps(task), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        response = self.app.delete('/api/tasks/1')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```