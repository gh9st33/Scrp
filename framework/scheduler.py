```python
from celery import Celery
from celery.schedules import crontab
from scraper_manager import ScraperManager

# Initialize Celery
app = Celery('scheduler', broker='pyamqp://guest@localhost//')

# Initialize ScraperManager
scraper_manager = ScraperManager()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, scraper_manager.run_scrapers.s('hello'), name='Run scrapers every 10')

@app.task
def run_scrapers(arg):
    print(f'Running scrapers: {arg}')
    scraper_manager.run()

if __name__ == "__main__":
    app.start()
```
This Python script uses the Celery library to schedule tasks. It sets up a periodic task that calls the `run_scrapers` function every 10 seconds. The `run_scrapers` function is a Celery task that prints a message and then calls the `run` method of the `ScraperManager` object. The `ScraperManager` object is responsible for managing the scrapers.