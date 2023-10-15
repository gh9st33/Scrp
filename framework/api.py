```python
from flask import Flask, request, jsonify
from task_queue import TaskQueue
from scraper import Scraper
from scheduler import Scheduler
from error_handler import ErrorHandler
from data_storage import DataStorage
from scrapy_integration import ScrapyIntegration
from scrapyd_integration import ScrapydIntegration

app = Flask(__name__)

task_queue = TaskQueue()
scheduler = Scheduler()
error_handler = ErrorHandler()
data_storage = DataStorage()
scrapy_integration = ScrapyIntegration()
scrapyd_integration = ScrapydIntegration()

@app.route('/api/tasks', methods=['POST'])
def add_task():
    task_data = request.get_json()
    try:
        task_queue.add_task(task_data)
        return jsonify({'message': 'Task added successfully'}), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'message': 'Failed to add task'}), 500

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = task_queue.get_tasks()
        return jsonify(tasks), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'message': 'Failed to retrieve tasks'}), 500

@app.route('/api/scrapers', methods=['POST'])
def deploy_scraper():
    scraper_data = request.get_json()
    try:
        scraper = Scraper(scraper_data)
        scheduler.schedule(scraper)
        return jsonify({'message': 'Scraper deployed successfully'}), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'message': 'Failed to deploy scraper'}), 500

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        data = data_storage.get_data()
        return jsonify(data), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'message': 'Failed to retrieve data'}), 500

@app.route('/api/logs', methods=['GET'])
def get_logs():
    try:
        logs = error_handler.get_logs()
        return jsonify(logs), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'message': 'Failed to retrieve logs'}), 500

@app.route('/api/scrapy', methods=['POST'])
def integrate_scrapy():
    try:
        scrapy_integration.integrate()
        return jsonify({'message': 'Scrapy integrated successfully'}), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'message': 'Failed to integrate Scrapy'}), 500

@app.route('/api/scrapyd', methods=['POST'])
def integrate_scrapyd():
    try:
        scrapyd_integration.integrate()
        return jsonify({'message': 'Scrapyd integrated successfully'}), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'message': 'Failed to integrate Scrapyd'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```