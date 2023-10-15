```python
from flask import Flask, request, jsonify
from task_queue import TaskQueue
from scraper import Scraper
from error_handler import ErrorHandler
from data_storage import DataStorage

app = Flask(__name__)
task_queue = TaskQueue()
scraper = Scraper()
error_handler = ErrorHandler()
data_storage = DataStorage()

@app.route('/api/tasks', methods=['POST'])
def add_task():
    task = request.get_json()
    try:
        task_queue.add_task(task)
        return jsonify({'message': 'Task added successfully'}), 200
    except Exception as e:
        error_handler.log_error(str(e))
        return jsonify({'message': 'Failed to add task'}), 500

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = task_queue.get_tasks()
        return jsonify({'tasks': tasks}), 200
    except Exception as e:
        error_handler.log_error(str(e))
        return jsonify({'message': 'Failed to retrieve tasks'}), 500

@app.route('/api/scrape', methods=['POST'])
def start_scrape():
    task = request.get_json()
    try:
        scraper.start_scrape(task)
        return jsonify({'message': 'Scrape started successfully'}), 200
    except Exception as e:
        error_handler.log_error(str(e))
        return jsonify({'message': 'Failed to start scrape'}), 500

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        data = data_storage.get_data()
        return jsonify({'data': data}), 200
    except Exception as e:
        error_handler.log_error(str(e))
        return jsonify({'message': 'Failed to retrieve data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```