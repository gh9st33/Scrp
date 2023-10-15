```python
from flask import Blueprint, jsonify
from flask_login import login_required
from .models import Log, Metric

logs_metrics = Blueprint('logs_metrics', __name__)

@logs_metrics.route('/logs', methods=['GET'])
@login_required
def get_logs():
    logs = Log.query.all()
    return jsonify([log.serialize() for log in logs]), 200

@logs_metrics.route('/metrics', methods=['GET'])
@login_required
def get_metrics():
    metrics = Metric.query.all()
    return jsonify([metric.serialize() for metric in metrics]), 200
```