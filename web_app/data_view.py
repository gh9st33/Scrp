```python
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from .models import Task, Data

data_view = Blueprint('data_view', __name__)

@data_view.route('/data', methods=['GET'])
@jwt_required
def get_data():
    task_id = request.args.get('task_id')
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    data = Data.query.filter_by(task_id=task_id).all()
    return jsonify([datum.to_dict() for datum in data]), 200

@data_view.route('/data/<data_id>', methods=['GET'])
@jwt_required
def get_data_by_id(data_id):
    data = Data.query.get(data_id)
    if not data:
        return jsonify({'message': 'Data not found'}), 404
    return jsonify(data.to_dict()), 200

@data_view.route('/data/<data_id>/download', methods=['GET'])
@jwt_required
def download_data(data_id):
    data = Data.query.get(data_id)
    if not data:
        return jsonify({'message': 'Data not found'}), 404
    response = make_response(data.content)
    response.headers.set('Content-Type', data.content_type)
    response.headers.set('Content-Disposition', 'attachment', filename=data.filename)
    return response
```