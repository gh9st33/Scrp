```python
import logging

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger('scraper')
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, error_message):
        self.logger.error(error_message)

    def log_info(self, info_message):
        self.logger.info(info_message)

    def log_warning(self, warning_message):
        self.logger.warning(warning_message)

    def log_critical(self, critical_message):
        self.logger.critical(critical_message)

    def log_exception(self, exception):
        self.logger.exception(exception)
```