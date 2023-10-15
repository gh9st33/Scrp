```python
import unittest
from scraper import Scraper

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper()

    def test_scrape(self):
        url = "http://example.com"
        data = self.scraper.scrape(url)
        self.assertIsNotNone(data)

    def test_scrape_invalid_url(self):
        url = "invalid_url"
        with self.assertRaises(ValueError):
            self.scraper.scrape(url)

    def test_scrape_no_data(self):
        url = "http://example.com/no_data"
        data = self.scraper.scrape(url)
        self.assertIsNone(data)

    def test_distribute_task(self):
        task = {"url": "http://example.com", "type": "data"}
        success = self.scraper.distribute_task(task)
        self.assertTrue(success)

    def test_distribute_task_invalid(self):
        task = {"url": "invalid_url", "type": "data"}
        with self.assertRaises(ValueError):
            self.scraper.distribute_task(task)

    def test_distribute_task_no_type(self):
        task = {"url": "http://example.com"}
        with self.assertRaises(KeyError):
            self.scraper.distribute_task(task)

if __name__ == '__main__':
    unittest.main()
```