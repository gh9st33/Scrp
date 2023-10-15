```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .authentication import UserSession
from .scraper_creator import create_scraper
from .scraper_updater import update_scraper
from .ssh_deployer import deploy_scraper

node_editor_bp = Blueprint('node_editor', __name__)

@node_editor_bp.route('/create_scraper', methods=['POST'])
@jwt_required()
def create():
    user_session = UserSession.get_from_jwt()
    scraper_config = request.json.get('scraper_config')
    scraper_id = create_scraper(user_session, scraper_config)
    return jsonify({'scraper_id': scraper_id}), 201

@node_editor_bp.route('/update_scraper/<scraper_id>', methods=['PUT'])
@jwt_required()
def update(scraper_id):
    user_session = UserSession.get_from_jwt()
    scraper_config = request.json.get('scraper_config')
    update_scraper(user_session, scraper_id, scraper_config)
    return jsonify({'message': 'Scraper updated successfully'}), 200

@node_editor_bp.route('/deploy_scraper/<scraper_id>', methods=['POST'])
@jwt_required()
def deploy(scraper_id):
    user_session = UserSession.get_from_jwt()
    server_config = request.json.get('server_config')
    deploy_scraper(user_session, scraper_id, server_config)
    return jsonify({'message': 'Scraper deployed successfully'}), 200
```