```python
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from task_queue import TaskQueue

class MySpider(scrapy.Spider):
    name = 'my_spider'

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        # This method should be overridden with the custom logic for parsing the response data
        pass

class ScraperManager:
    def __init__(self):
        self.task_queue = TaskQueue()
        self.process = CrawlerProcess(get_project_settings())

    def add_scraper_task(self, start_url):
        self.task_queue.add_task(self.run_spider, start_url)

    def run_spider(self, start_url):
        self.process.crawl(MySpider, start_url=start_url)

    def start(self):
        while not self.task_queue.is_empty():
            task, args = self.task_queue.get_task()
            task(*args)

        self.process.start()  # the script will block here until all crawling jobs are finished

if __name__ == "__main__":
    scraper_manager = ScraperManager()
    scraper_manager.start()
```