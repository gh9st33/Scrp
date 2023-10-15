```python
import unittest
from framework.data_storage import DataStorage

class TestDataStorage(unittest.TestCase):

    def setUp(self):
        self.data_storage = DataStorage()

    def test_store_data(self):
        data = {"name": "test", "value": "123"}
        self.data_storage.store_data(data)
        stored_data = self.data_storage.get_data("test")
        self.assertEqual(stored_data, "123")

    def test_get_data(self):
        data = {"name": "test", "value": "123"}
        self.data_storage.store_data(data)
        stored_data = self.data_storage.get_data("test")
        self.assertEqual(stored_data, "123")

    def test_delete_data(self):
        data = {"name": "test", "value": "123"}
        self.data_storage.store_data(data)
        self.data_storage.delete_data("test")
        stored_data = self.data_storage.get_data("test")
        self.assertIsNone(stored_data)

if __name__ == '__main__':
    unittest.main()
```