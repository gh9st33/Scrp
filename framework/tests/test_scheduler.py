```python
import unittest
from unittest.mock import patch
from scheduler import Scheduler

class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    @patch('scheduler.celery')
    def test_schedule_scraper(self, mock_celery):
        task_id = '123'
        schedule_time = '10:00'
        self.scheduler.schedule_scraper(task_id, schedule_time)
        mock_celery.add_periodic_task.assert_called_once_with(schedule_time, task_id)

    @patch('scheduler.celery')
    def test_remove_scheduled_scraper(self, mock_celery):
        task_id = '123'
        self.scheduler.remove_scheduled_scraper(task_id)
        mock_celery.control.revoke.assert_called_once_with(task_id)

    @patch('scheduler.celery')
    def test_get_scheduled_tasks(self, mock_celery):
        self.scheduler.get_scheduled_tasks()
        mock_celery.control.inspect.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```