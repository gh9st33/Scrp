```python
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from scrapy.exceptions import NotConfigured

class ScrapyIntegration:
    def __init__(self):
        self.process = None

    def start_scrapy(self):
        try:
            settings = get_project_settings()
            self.process = CrawlerProcess(settings)
        except NotConfigured as e:
            print(f"Scrapy not configured properly: {str(e)}")

    def add_spider(self, spider):
        if self.process:
            self.process.crawl(spider)
        else:
            print("Scrapy process not started. Call start_scrapy() first.")

    def run_scrapy(self):
        if self.process:
            self.process.start()
        else:
            print("Scrapy process not started. Call start_scrapy() first.")

    def stop_scrapy(self):
        if self.process:
            self.process.stop()
        else:
            print("Scrapy process not started. Call start_scrapy() first.")
```