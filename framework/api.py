```python
from flask import Flask, request, jsonify
from scraper import ScraperTask
from distributed import distribute_task
from queue import add_to_queue
from error_handler import handle_error
from data_storage import store_data

app = Flask(__name__)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        task = ScraperTask(data)
        distribute_task(task)
        add_to_queue(task)
        return jsonify({'message': 'Task created and distributed successfully'}), 201
    except Exception as e:
        handle_error(e)
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = ScraperTask.get(task_id)
        return jsonify(task.to_dict()), 200
    except Exception as e:
        handle_error(e)
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks/<task_id>/data', methods=['GET'])
def get_task_data(task_id):
    try:
        data = store_data.get(task_id)
        return jsonify(data), 200
    except Exception as e:
        handle_error(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```