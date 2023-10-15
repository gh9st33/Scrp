```python
from flask import Blueprint, request, jsonify
from framework.scraper_manager import ScraperManager
from framework.data_storage import DataStorage
from web_app.authentication import login_required, current_user

scraper_creator = Blueprint('scraper_creator', __name__)

@scraper_creator.route('/create_scraper', methods=['POST'])
@login_required
def create_scraper():
    data = request.get_json()
    scraper_name = data.get('scraper_name')
    scraper_config = data.get('scraper_config')

    if not scraper_name or not scraper_config:
        return jsonify({'message': 'Missing required parameters'}), 400

    scraper_manager = ScraperManager()
    created = scraper_manager.create_scraper(scraper_name, scraper_config, current_user.id)

    if not created:
        return jsonify({'message': 'Failed to create scraper'}), 500

    return jsonify({'message': 'Scraper created successfully'}), 200

@scraper_creator.route('/get_scraper_config_template', methods=['GET'])
@login_required
def get_scraper_config_template():
    scraper_manager = ScraperManager()
    template = scraper_manager.get_scraper_config_template()

    if not template:
        return jsonify({'message': 'Failed to retrieve scraper config template'}), 500

    return jsonify({'template': template}), 200
```