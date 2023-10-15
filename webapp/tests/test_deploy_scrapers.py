```python
import unittest
from flask import Flask
from webapp.deploy_scrapers import DeployScrapers

class TestDeployScrapers(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        self.deploy_scrapers = DeployScrapers()

    def test_deploy_scraper(self):
        response = self.client.post('/deploy', data={'scraper_name': 'test_scraper', 'url': 'http://test.com'})
        self.assertEqual(response.status_code, 200)

    def test_get_all_scrapers(self):
        response = self.client.get('/scrapers')
        self.assertEqual(response.status_code, 200)

    def test_get_scraper_by_name(self):
        response = self.client.get('/scrapers/test_scraper')
        self.assertEqual(response.status_code, 200)

    def test_delete_scraper(self):
        response = self.client.delete('/scrapers/test_scraper')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```