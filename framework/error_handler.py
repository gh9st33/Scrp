```python
import logging

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger('scraper')
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def log_error(self, error_message):
        self.logger.error(error_message)

    def log_info(self, info_message):
        self.logger.info(info_message)

    def log_warning(self, warning_message):
        self.logger.warning(warning_message)

    def log_debug(self, debug_message):
        self.logger.debug(debug_message)

error_handler = ErrorHandler()
```