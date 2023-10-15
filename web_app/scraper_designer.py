```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from framework.scraper_manager import ScraperManager
from framework.data_storage import DataStorage

scraper_designer = Blueprint('scraper_designer', __name__)
scraper_manager = ScraperManager()
data_storage = DataStorage()

@scraper_designer.route('/design_scraper', methods=['POST'])
@jwt_required
def design_scraper():
    scraper_config = request.json
    try:
        scraper_manager.validate_scraper_config(scraper_config)
        scraper_id = scraper_manager.create_scraper(scraper_config)
        return jsonify({'message': 'Scraper created successfully', 'scraper_id': scraper_id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@scraper_designer.route('/update_scraper/<scraper_id>', methods=['PUT'])
@jwt_required
def update_scraper(scraper_id):
    scraper_config = request.json
    try:
        scraper_manager.validate_scraper_config(scraper_config)
        scraper_manager.update_scraper(scraper_id, scraper_config)
        return jsonify({'message': 'Scraper updated successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@scraper_designer.route('/delete_scraper/<scraper_id>', methods=['DELETE'])
@jwt_required
def delete_scraper(scraper_id):
    try:
        scraper_manager.delete_scraper(scraper_id)
        return jsonify({'message': 'Scraper deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@scraper_designer.route('/get_scraper/<scraper_id>', methods=['GET'])
@jwt_required
def get_scraper(scraper_id):
    try:
        scraper_config = scraper_manager.get_scraper(scraper_id)
        return jsonify({'scraper_config': scraper_config}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@scraper_designer.route('/get_all_scrapers', methods=['GET'])
@jwt_required
def get_all_scrapers():
    try:
        scrapers = scraper_manager.get_all_scrapers()
        return jsonify({'scrapers': scrapers}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
```