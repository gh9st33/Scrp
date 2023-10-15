```python
import unittest
from scrapy_app.items import MyItem

class TestMyItem(unittest.TestCase):

    def setUp(self):
        self.item = MyItem()

    def test_fields(self):
        self.assertEqual(set(self.item.fields.keys()), {'field1', 'field2', 'field3'})

    def test_set_and_get_field(self):
        self.item['field1'] = 'value1'
        self.assertEqual(self.item['field1'], 'value1')

    def test_set_and_get_nonexistent_field(self):
        with self.assertRaises(KeyError):
            self.item['nonexistent_field'] = 'value'

if __name__ == '__main__':
    unittest.main()
```