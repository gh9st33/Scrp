```python
import unittest
from framework.scheduler import Scheduler

class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def test_schedule_task(self):
        task_id = "123"
        time = "10:00"
        self.scheduler.schedule_task(task_id, time)
        self.assertIn(task_id, self.scheduler.tasks)

    def test_remove_task(self):
        task_id = "123"
        self.scheduler.schedule_task(task_id, "10:00")
        self.scheduler.remove_task(task_id)
        self.assertNotIn(task_id, self.scheduler.tasks)

    def test_reschedule_task(self):
        task_id = "123"
        old_time = "10:00"
        new_time = "11:00"
        self.scheduler.schedule_task(task_id, old_time)
        self.scheduler.reschedule_task(task_id, new_time)
        self.assertEqual(self.scheduler.tasks[task_id], new_time)

if __name__ == '__main__':
    unittest.main()
```