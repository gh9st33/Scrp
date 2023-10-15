```python
from flask import Flask
from api import api_bp
from scheduler import scheduler_bp
from distributed import distributed_bp
from queue import queue_bp
from scraper import scraper_bp
from data_storage import data_storage_bp
from error_handler import error_handler_bp

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(api_bp)
app.register_blueprint(scheduler_bp)
app.register_blueprint(distributed_bp)
app.register_blueprint(queue_bp)
app.register_blueprint(scraper_bp)
app.register_blueprint(data_storage_bp)
app.register_blueprint(error_handler_bp)

if __name__ == "__main__":
    app.run(debug=True)
```