```python
from flask import Flask, request, jsonify
from scraper_manager import ScraperManager
from task_queue import TaskQueue
from data_storage import DataStorage
from error_handler import ErrorHandler

app = Flask(__name__)
scraper_manager = ScraperManager()
task_queue = TaskQueue()
data_storage = DataStorage()
error_handler = ErrorHandler()

@app.route('/api/v1/tasks', methods=['POST'])
def create_task():
    try:
        task_data = request.get_json()
        task_id = scraper_manager.create_task(task_data)
        return jsonify({'task_id': task_id}), 201
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = scraper_manager.get_task(task_id)
        return jsonify(task), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        scraper_manager.delete_task(task_id)
        return '', 204
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1/tasks/<task_id>/data', methods=['GET'])
def get_task_data(task_id):
    try:
        data = data_storage.get_data(task_id)
        return jsonify(data), 200
    except Exception as e:
        error_handler.log_error(e)
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```