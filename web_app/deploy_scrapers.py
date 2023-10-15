```python
from flask import Blueprint, request, jsonify
from framework.task_queue import add_task
from framework.scraper import deploy_scraper

deploy_scrapers_bp = Blueprint('deploy_scrapers', __name__)

@deploy_scrapers_bp.route('/deploy', methods=['POST'])
def deploy():
    data = request.get_json()
    scraper_name = data.get('scraper_name')
    scraper_config = data.get('scraper_config')

    if not scraper_name or not scraper_config:
        return jsonify({'message': 'Missing scraper name or configuration'}), 400

    try:
        # Deploy the scraper
        deploy_scraper(scraper_name, scraper_config)

        # Add the scraper task to the queue
        add_task(scraper_name)

        return jsonify({'message': 'Scraper deployed successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to deploy scraper', 'error': str(e)}), 500
```