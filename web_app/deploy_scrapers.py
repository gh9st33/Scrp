```python
from flask import Blueprint, request, jsonify
from framework.scraper_manager import ScraperManager
from framework.api import api
from web_app.authentication import login_required

deploy_scrapers = Blueprint('deploy_scrapers', __name__)

scraper_manager = ScraperManager()

@deploy_scrapers.route('/deploy', methods=['POST'])
@login_required
def deploy():
    data = request.get_json()
    scraper_config = data.get('scraper_config')
    if not scraper_config:
        return jsonify({'error': 'No scraper configuration provided'}), 400

    try:
        scraper_id = scraper_manager.deploy_scraper(scraper_config)
        return jsonify({'message': 'Scraper deployed successfully', 'scraper_id': scraper_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/scrapers', methods=['GET'])
@login_required
def get_scrapers():
    try:
        scrapers = scraper_manager.get_scrapers()
        return jsonify({'scrapers': scrapers}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```