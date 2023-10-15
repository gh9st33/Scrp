```python
from flask import Blueprint, request, jsonify
from framework.api import deploy_scraper
from framework.ssh_deployment import deploy_agent
from web_app.user_auth import login_required

deploy_blueprint = Blueprint('deploy', __name__)

@deploy_blueprint.route('/deploy_scraper', methods=['POST'])
@login_required
def deploy():
    data = request.get_json()
    scraper_definition = data.get('scraper_definition')
    target_url = data.get('target_url')
    additional_parameters = data.get('additional_parameters')

    try:
        deploy_scraper(scraper_definition, target_url, additional_parameters)
        return jsonify({'message': 'Scraper deployed successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to deploy scraper', 'error': str(e)}), 400

@deploy_blueprint.route('/deploy_agent', methods=['POST'])
@login_required
def deploy_agent():
    data = request.get_json()
    server_ip = data.get('server_ip')
    ssh_key = data.get('ssh_key')

    try:
        deploy_agent(server_ip, ssh_key)
        return jsonify({'message': 'Agent deployed successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to deploy agent', 'error': str(e)}), 400
```