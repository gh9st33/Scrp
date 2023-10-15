```python
from flask import Flask
from api import api_bp
from task_queue import init_queue
from scheduler import init_scheduler
from data_storage import init_db
from error_handler import init_error_handler

app = Flask(__name__)

# Initialize components
init_db(app)
init_queue(app)
init_scheduler(app)
init_error_handler(app)

# Register API blueprint
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```