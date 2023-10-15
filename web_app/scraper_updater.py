```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from scraper_manager import update_scraper

scraper_updater_bp = Blueprint('scraper_updater_bp', __name__)

@scraper_updater_bp.route('/update_scraper', methods=['POST'])
@jwt_required
def update_scraper_endpoint():
    user_id = get_jwt_identity()
    scraper_data = request.get_json()

    if not scraper_data:
        return jsonify({"msg": "Missing JSON in request"}), 400

    scraper_id = scraper_data.get('scraper_id', None)
    new_config = scraper_data.get('new_config', None)

    if not scraper_id or not new_config:
        return jsonify({"msg": "Missing scraper_id or new_config in JSON"}), 400

    try:
        update_scraper(user_id, scraper_id, new_config)
        return jsonify({"msg": "Scraper updated successfully"}), 200
    except Exception as e:
        return jsonify({"msg": "Failed to update scraper", "error": str(e)}), 500
```