```python
from celery import Celery
from celery.schedules import crontab
from task_queue import add_task_to_queue

app = Celery('scheduler', broker='pyamqp://guest@localhost//')

# Define the schedule
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add_to_queue',
        'schedule': 30.0,
    },
}

@app.task
def add_to_queue():
    # Get the tasks from the database or API
    tasks = get_tasks()
    for task in tasks:
        add_task_to_queue(task)

def get_tasks():
    # This function should interact with the database or API to get the tasks
    # For now, we will just return a list of tasks
    return ['task1', 'task2', 'task3']

if __name__ == "__main__":
    app.start()
```