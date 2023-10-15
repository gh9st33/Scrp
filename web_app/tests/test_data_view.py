```python
import unittest
from flask import Flask
from flask_testing import TestCase
from data_view import DataView

class TestDataView(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.data_view = DataView()

    def tearDown(self):
        pass

    def test_get_data(self):
        response = self.data_view.get_data()
        self.assertEqual(response.status_code, 200)

    def test_download_data(self):
        response = self.data_view.download_data()
        self.assertEqual(response.status_code, 200)

    def test_view_images(self):
        response = self.data_view.view_images()
        self.assertEqual(response.status_code, 200)

    def test_download_images(self):
        response = self.data_view.download_images()
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```