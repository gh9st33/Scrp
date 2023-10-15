```python
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server import db

logs_metrics = Blueprint('logs_metrics', __name__)

@logs_metrics.route('/logs', methods=['GET'])
@jwt_required
def get_logs():
    logs = db.logs.find()
    return jsonify({'logs': logs}), 200

@logs_metrics.route('/metrics', methods=['GET'])
@jwt_required
def get_metrics():
    metrics = db.metrics.find()
    return jsonify({'metrics': metrics}), 200

@logs_metrics.route('/logs/<id>', methods=['GET'])
@jwt_required
def get_log(id):
    log = db.logs.find_one({'_id': id})
    if log:
        return jsonify({'log': log}), 200
    else:
        return jsonify({'error': 'Log not found'}), 404

@logs_metrics.route('/metrics/<id>', methods=['GET'])
@jwt_required
def get_metric(id):
    metric = db.metrics.find_one({'_id': id})
    if metric:
        return jsonify({'metric': metric}), 200
    else:
        return jsonify({'error': 'Metric not found'}), 404
```