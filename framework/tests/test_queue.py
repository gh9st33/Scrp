```python
import unittest
from framework.queue import TaskQueue

class TestTaskQueue(unittest.TestCase):

    def setUp(self):
        self.queue = TaskQueue()

    def test_enqueue(self):
        task = {"id": 1, "task": "scrape", "url": "http://example.com"}
        self.queue.enqueue(task)
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue(self):
        task = {"id": 1, "task": "scrape", "url": "http://example.com"}
        self.queue.enqueue(task)
        dequeued_task = self.queue.dequeue()
        self.assertEqual(dequeued_task, task)

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        task = {"id": 1, "task": "scrape", "url": "http://example.com"}
        self.queue.enqueue(task)
        self.assertEqual(self.queue.size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        task = {"id": 1, "task": "scrape", "url": "http://example.com"}
        self.queue.enqueue(task)
        self.assertFalse(self.queue.is_empty())

if __name__ == '__main__':
    unittest.main()
```