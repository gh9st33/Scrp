```python
import unittest
from flask import Flask
from web_app.deploy_scrapers import deploy_scraper

class TestDeployScrapers(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_deploy_scraper(self):
        response = self.client.post('/deploy_scraper', data={'scraper_name': 'test_scraper'})
        self.assertEqual(response.status_code, 200)

    def test_deploy_scraper_without_name(self):
        response = self.client.post('/deploy_scraper', data={})
        self.assertEqual(response.status_code, 400)

    def test_deploy_scraper_with_invalid_name(self):
        response = self.client.post('/deploy_scraper', data={'scraper_name': 'invalid_scraper'})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
```