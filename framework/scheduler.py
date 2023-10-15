```python
from celery import Celery
from celery.schedules import crontab
from scraper import ScraperTask

# Initialize Celery
app = Celery('scheduler', broker='pyamqp://guest@localhost//')

# Define the schedule
app.conf.beat_schedule = {
    'run-every-30-minutes': {
        'task': 'tasks.run_scraper',
        'schedule': crontab(minute='*/30'),
    },
}

@app.task
def run_scraper():
    scraper_task = ScraperTask()
    scraper_task.run()

if __name__ == "__main__":
    app.start()
```