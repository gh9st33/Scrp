```python
from flask import Blueprint, jsonify, request
from framework.error_handler import get_error_log
from framework.api import get_scraper_metrics

logs_metrics_bp = Blueprint('logs_metrics', __name__)

@logs_metrics_bp.route('/logs', methods=['GET'])
def get_logs():
    try:
        logs = get_error_log()
        return jsonify({'status': 'success', 'data': logs}), 200
    except Exception as e:
        return jsonify({'status': 'fail', 'message': str(e)}), 500

@logs_metrics_bp.route('/metrics', methods=['GET'])
def get_metrics():
    try:
        scraper_id = request.args.get('scraper_id')
        metrics = get_scraper_metrics(scraper_id)
        return jsonify({'status': 'success', 'data': metrics}), 200
    except Exception as e:
        return jsonify({'status': 'fail', 'message': str(e)}), 500
```