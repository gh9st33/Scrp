```python
import unittest
from framework.scraper import Scraper, ScraperTask

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper()
        self.task = ScraperTask('http://example.com', 'GET')

    def test_create_task(self):
        task = self.scraper.create_task('http://example.com', 'GET')
        self.assertIsInstance(task, ScraperTask)

    def test_add_task_to_queue(self):
        self.scraper.add_task_to_queue(self.task)
        self.assertIn(self.task, self.scraper.task_queue)

    def test_remove_task_from_queue(self):
        self.scraper.add_task_to_queue(self.task)
        self.scraper.remove_task_from_queue(self.task)
        self.assertNotIn(self.task, self.scraper.task_queue)

    def test_execute_task(self):
        result = self.scraper.execute_task(self.task)
        self.assertIsNotNone(result)

    def test_handle_error(self):
        with self.assertRaises(Exception):
            self.scraper.handle_error(Exception('Test error'))

if __name__ == '__main__':
    unittest.main()
```