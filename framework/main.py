```python
from flask import Flask
from api import Api
from task_queue import TaskQueue
from scheduler import Scheduler
from data_storage import DataStorage
from error_handler import ErrorHandler
from scrapy_integration import ScrapyIntegration
from scrapyd_integration import ScrapydIntegration
from ssh_deployment import SSHDeployment

app = Flask(__name__)
api = Api(app)
task_queue = TaskQueue()
scheduler = Scheduler()
data_storage = DataStorage()
error_handler = ErrorHandler()
scrapy_integration = ScrapyIntegration()
scrapyd_integration = ScrapydIntegration()
ssh_deployment = SSHDeployment()

if __name__ == "__main__":
    try:
        # Initialize the components
        api.initialize()
        task_queue.initialize()
        scheduler.initialize()
        data_storage.initialize()
        error_handler.initialize()
        scrapy_integration.initialize()
        scrapyd_integration.initialize()
        ssh_deployment.initialize()

        # Start the Flask server
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        error_handler.handle(e)
```