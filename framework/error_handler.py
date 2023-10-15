```python
import logging
from logging.handlers import RotatingFileHandler

# Define error codes
SCRAPER_NOT_FOUND = 1001
TASK_NOT_FOUND = 1002
INVALID_SCRAPER_CONFIG = 1003
SCRAPER_EXECUTION_ERROR = 1004
DATABASE_CONNECTION_ERROR = 1005
UNEXPECTED_ERROR = 9999

# Define error messages
error_messages = {
    SCRAPER_NOT_FOUND: "Scraper not found",
    TASK_NOT_FOUND: "Task not found",
    INVALID_SCRAPER_CONFIG: "Invalid scraper configuration",
    SCRAPER_EXECUTION_ERROR: "Error occurred during scraper execution",
    DATABASE_CONNECTION_ERROR: "Database connection error",
    UNEXPECTED_ERROR: "Unexpected error occurred"
}

# Set up logging
logger = logging.getLogger('scraper_error_logger')
logger.setLevel(logging.ERROR)
handler = RotatingFileHandler('scraper_errors.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

def log_error(error_code, details=None):
    error_message = error_messages.get(error_code, "Unknown error")
    if details:
        error_message += f" - Details: {details}"
    logger.error(error_message)

def handle_error(error_code, details=None):
    log_error(error_code, details)
    return {
        "error": True,
        "code": error_code,
        "message": error_messages.get(error_code, "Unknown error")
    }
```