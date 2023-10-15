```python
import unittest
from scrapy_app import settings

class TestSettings(unittest.TestCase):

    def test_bot_name(self):
        self.assertEqual(settings.BOT_NAME, 'scrapy_app')

    def test_spider_modules(self):
        self.assertEqual(settings.SPIDER_MODULES, ['scrapy_app.spiders'])

    def test_newspider_module(self):
        self.assertEqual(settings.NEWSPIDER_MODULE, 'scrapy_app.spiders')

    def test_robotstxt_obey(self):
        self.assertEqual(settings.ROBOTSTXT_OBEY, True)

    def test_item_pipelines(self):
        self.assertEqual(settings.ITEM_PIPELINES, {'scrapy_app.pipelines.ScrapyAppPipeline': 300})

    def test_mongodb_server(self):
        self.assertEqual(settings.MONGODB_SERVER, "localhost")

    def test_mongodb_port(self):
        self.assertEqual(settings.MONGODB_PORT, 27017)

    def test_mongodb_db(self):
        self.assertEqual(settings.MONGODB_DB, "scrapy_app")

    def test_mongodb_collection(self):
        self.assertEqual(settings.MONGODB_COLLECTION, "scraped_data")

if __name__ == '__main__':
    unittest.main()
```