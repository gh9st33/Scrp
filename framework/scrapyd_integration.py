```python
import json
import requests
from framework.error_handler import ErrorHandler

class ScrapydIntegration:
    def __init__(self, scrapyd_url):
        self.scrapyd_url = scrapyd_url
        self.error_handler = ErrorHandler()

    def schedule_spider(self, project_name, spider_name, settings=None, _job=None):
        try:
            url = f"{self.scrapyd_url}/schedule.json"
            data = {
                'project': project_name,
                'spider': spider_name,
                'setting': settings,
                '_job': _job
            }
            response = requests.post(url, data=data)
            return response.json()
        except Exception as e:
            self.error_handler.log_error(e)
            return None

    def cancel_spider(self, project_name, job_id):
        try:
            url = f"{self.scrapyd_url}/cancel.json"
            data = {
                'project': project_name,
                'job': job_id
            }
            response = requests.post(url, data=data)
            return response.json()
        except Exception as e:
            self.error_handler.log_error(e)
            return None

    def list_spiders(self, project_name):
        try:
            url = f"{self.scrapyd_url}/listspiders.json"
            params = {'project': project_name}
            response = requests.get(url, params=params)
            return response.json()
        except Exception as e:
            self.error_handler.log_error(e)
            return None

    def list_jobs(self, project_name):
        try:
            url = f"{self.scrapyd_url}/listjobs.json"
            params = {'project': project_name}
            response = requests.get(url, params=params)
            return response.json()
        except Exception as e:
            self.error_handler.log_error(e)
            return None
```