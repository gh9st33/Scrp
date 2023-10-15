```python
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from data_storage import DataStorage
from error_handler import ErrorHandler

class Scraper(scrapy.Spider):
    name = "scraper"
    start_urls = []

    def __init__(self, target_urls=None, *args, **kwargs):
        super(Scraper, self).__init__(*args, **kwargs)
        if target_urls is not None:
            self.start_urls = target_urls

    def parse(self, response):
        # This method should be overridden with the custom scraping logic
        pass

class ScraperManager:
    def __init__(self):
        self.data_storage = DataStorage()
        self.error_handler = ErrorHandler()

    def run_scraper(self, scraper, target_urls):
        process = CrawlerProcess(get_project_settings())
        process.crawl(scraper, target_urls=target_urls)
        process.start()

    def handle_data(self, data):
        try:
            self.data_storage.store_data(data)
        except Exception as e:
            self.error_handler.log_error(str(e))

    def handle_error(self, error):
        self.error_handler.log_error(error)
```