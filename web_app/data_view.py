```python
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from framework.data_storage import get_data

data_view = Blueprint('data_view', __name__)

@data_view.route('/data', methods=['GET'])
@jwt_required
def view_data():
    scraper_id = request.args.get('scraper_id')
    if not scraper_id:
        return jsonify({'error': 'Missing scraper_id'}), 400

    data = get_data(scraper_id)
    if data is None:
        return jsonify({'error': 'No data found for given scraper_id'}), 404

    return jsonify(data), 200

@data_view.route('/data/download', methods=['GET'])
@jwt_required
def download_data():
    scraper_id = request.args.get('scraper_id')
    if not scraper_id:
        return jsonify({'error': 'Missing scraper_id'}), 400

    data = get_data(scraper_id)
    if data is None:
        return jsonify({'error': 'No data found for given scraper_id'}), 404

    response = jsonify(data)
    response.headers['Content-Disposition'] = f'attachment; filename={scraper_id}_data.json'
    return response
```