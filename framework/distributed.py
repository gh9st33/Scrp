```python
import os
from multiprocessing import Pool
from scraper import ScraperTask

class DistributedScraper:
    def __init__(self, num_workers=None):
        self.num_workers = num_workers if num_workers else os.cpu_count()

    def distribute_tasks(self, tasks):
        with Pool(processes=self.num_workers) as pool:
            results = pool.map(self.execute_task, tasks)
        return results

    @staticmethod
    def execute_task(task):
        scraper = ScraperTask(task)
        return scraper.run()
```