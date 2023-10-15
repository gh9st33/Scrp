```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import Node, Scraper
from . import db

node_editor = Blueprint('node_editor', __name__)

@node_editor.route('/nodes', methods=['GET'])
@jwt_required
def get_nodes():
    nodes = Node.query.all()
    return jsonify([node.to_dict() for node in nodes]), 200

@node_editor.route('/node', methods=['POST'])
@jwt_required
def create_node():
    data = request.get_json()
    new_node = Node(data)
    db.session.add(new_node)
    db.session.commit()
    return jsonify(new_node.to_dict()), 201

@node_editor.route('/node/<int:node_id>', methods=['PUT'])
@jwt_required
def update_node(node_id):
    data = request.get_json()
    node = Node.query.get(node_id)
    if not node:
        return jsonify({'message': 'Node not found'}), 404
    node.update(data)
    db.session.commit()
    return jsonify(node.to_dict()), 200

@node_editor.route('/node/<int:node_id>', methods=['DELETE'])
@jwt_required
def delete_node(node_id):
    node = Node.query.get(node_id)
    if not node:
        return jsonify({'message': 'Node not found'}), 404
    db.session.delete(node)
    db.session.commit()
    return jsonify({'message': 'Node deleted'}), 200

@node_editor.route('/node/<int:node_id>/scrapers', methods=['GET'])
@jwt_required
def get_node_scrapers(node_id):
    node = Node.query.get(node_id)
    if not node:
        return jsonify({'message': 'Node not found'}), 404
    scrapers = Scraper.query.filter_by(node_id=node_id).all()
    return jsonify([scraper.to_dict() for scraper in scrapers]), 200
```