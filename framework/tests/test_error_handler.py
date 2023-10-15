```python
import unittest
from unittest.mock import patch
from error_handler import ErrorHandler

class TestErrorHandler(unittest.TestCase):

    @patch('error_handler.logging')
    def test_log_error(self, mock_logging):
        error_handler = ErrorHandler()
        error_handler.log_error('Test error message')
        mock_logging.error.assert_called_once_with('Test error message')

    @patch('error_handler.logging')
    def test_log_warning(self, mock_logging):
        error_handler = ErrorHandler()
        error_handler.log_warning('Test warning message')
        mock_logging.warning.assert_called_once_with('Test warning message')

    @patch('error_handler.logging')
    def test_log_info(self, mock_logging):
        error_handler = ErrorHandler()
        error_handler.log_info('Test info message')
        mock_logging.info.assert_called_once_with('Test info message')

    @patch('error_handler.logging')
    def test_log_debug(self, mock_logging):
        error_handler = ErrorHandler()
        error_handler.log_debug('Test debug message')
        mock_logging.debug.assert_called_once_with('Test debug message')

if __name__ == '__main__':
    unittest.main()
```