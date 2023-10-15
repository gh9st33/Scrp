```python
import unittest
from task_queue import TaskQueue

class TestTaskQueue(unittest.TestCase):

    def setUp(self):
        self.task_queue = TaskQueue()

    def test_add_task(self):
        task = {"id": 1, "name": "Test Task", "status": "pending"}
        self.task_queue.add_task(task)
        self.assertIn(task, self.task_queue.tasks)

    def test_get_task(self):
        task = {"id": 1, "name": "Test Task", "status": "pending"}
        self.task_queue.add_task(task)
        retrieved_task = self.task_queue.get_task(1)
        self.assertEqual(task, retrieved_task)

    def test_remove_task(self):
        task = {"id": 1, "name": "Test Task", "status": "pending"}
        self.task_queue.add_task(task)
        self.task_queue.remove_task(1)
        self.assertNotIn(task, self.task_queue.tasks)

    def test_update_task_status(self):
        task = {"id": 1, "name": "Test Task", "status": "pending"}
        self.task_queue.add_task(task)
        self.task_queue.update_task_status(1, "completed")
        self.assertEqual("completed", self.task_queue.tasks[0]["status"])

if __name__ == '__main__':
    unittest.main()
```