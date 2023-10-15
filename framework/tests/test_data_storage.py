```python
import unittest
from framework.data_storage import DataStorage

class TestDataStorage(unittest.TestCase):

    def setUp(self):
        self.data_storage = DataStorage()

    def test_store_data(self):
        data = {"title": "Test Title", "description": "Test Description"}
        self.data_storage.store_data(data)
        stored_data = self.data_storage.get_data()
        self.assertEqual(data, stored_data)

    def test_store_image(self):
        image_path = "/path/to/image.jpg"
        self.data_storage.store_image(image_path)
        stored_image_path = self.data_storage.get_image()
        self.assertEqual(image_path, stored_image_path)

    def test_get_data(self):
        data = {"title": "Test Title", "description": "Test Description"}
        self.data_storage.store_data(data)
        retrieved_data = self.data_storage.get_data()
        self.assertEqual(data, retrieved_data)

    def test_get_image(self):
        image_path = "/path/to/image.jpg"
        self.data_storage.store_image(image_path)
        retrieved_image_path = self.data_storage.get_image()
        self.assertEqual(image_path, retrieved_image_path)

if __name__ == '__main__':
    unittest.main()
```