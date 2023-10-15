```python
import logging

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger('scraper_framework')
        self.logger.setLevel(logging.ERROR)
        handler = logging.FileHandler('error.log')
        handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, error_message):
        self.logger.error(error_message)

    def alert(self, error_message):
        # This function can be implemented to send alerts through email or other means
        pass
```