```python
import unittest
from webapp.data_view import DataView

class TestDataView(unittest.TestCase):

    def setUp(self):
        self.data_view = DataView()

    def test_get_data(self):
        data = self.data_view.get_data()
        self.assertIsNotNone(data, "Data should not be None")

    def test_download_data(self):
        response = self.data_view.download_data()
        self.assertEqual(response.status_code, 200, "Download data failed")

    def test_view_images(self):
        images = self.data_view.view_images()
        self.assertIsNotNone(images, "Images should not be None")

    def test_download_images(self):
        response = self.data_view.download_images()
        self.assertEqual(response.status_code, 200, "Download images failed")

if __name__ == '__main__':
    unittest.main()
```