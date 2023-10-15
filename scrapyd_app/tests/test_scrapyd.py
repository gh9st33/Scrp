```python
import unittest
from scrapyd_api import ScrapydAPI

class TestScrapyd(unittest.TestCase):
    def setUp(self):
        self.scrapyd = ScrapydAPI('http://localhost:6800')

    def test_list_projects(self):
        projects = self.scrapyd.list_projects()
        self.assertIsInstance(projects, list)

    def test_list_spiders(self):
        spiders = self.scrapyd.list_spiders('project_name')
        self.assertIsInstance(spiders, list)

    def test_schedule_spider(self):
        job_id = self.scrapyd.schedule('project_name', 'spider_name')
        self.assertIsInstance(job_id, str)

    def test_cancel_spider(self):
        cancel_status = self.scrapyd.cancel('project_name', 'job_id')
        self.assertEqual(cancel_status, 'cancelled')

    def test_delete_project(self):
        delete_status = self.scrapyd.delete_project('project_name')
        self.assertEqual(delete_status, 'ok')

if __name__ == '__main__':
    unittest.main()
```