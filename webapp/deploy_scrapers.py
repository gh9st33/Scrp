```python
from flask import Blueprint, request, jsonify
from framework.api import create_scraper_task

deploy_scrapers = Blueprint('deploy_scrapers', __name__)

@deploy_scrapers.route('/deploy', methods=['POST'])
def deploy():
    data = request.get_json()
    task_id = create_scraper_task(data)
    if task_id:
        return jsonify({'message': 'Scraper task created successfully', 'task_id': task_id}), 201
    else:
        return jsonify({'message': 'Failed to create scraper task'}), 400
```