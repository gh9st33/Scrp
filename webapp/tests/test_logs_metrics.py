```python
import unittest
from logs_metrics import LogsMetrics

class TestLogsMetrics(unittest.TestCase):

    def setUp(self):
        self.logs_metrics = LogsMetrics()

    def test_get_logs(self):
        logs = self.logs_metrics.get_logs()
        self.assertIsInstance(logs, list)

    def test_get_metrics(self):
        metrics = self.logs_metrics.get_metrics()
        self.assertIsInstance(metrics, dict)

    def test_get_log_by_id(self):
        log_id = 1
        log = self.logs_metrics.get_log_by_id(log_id)
        self.assertIsInstance(log, dict)

    def test_get_metric_by_id(self):
        metric_id = 1
        metric = self.logs_metrics.get_metric_by_id(metric_id)
        self.assertIsInstance(metric, dict)

if __name__ == '__main__':
    unittest.main()
```