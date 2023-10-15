```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import Scraper, db

scrapers_blueprint = Blueprint('scrapers', __name__)

@scrapers_blueprint.route('/design', methods=['POST'])
@jwt_required
def design_scraper():
    data = request.get_json()
    new_scraper = Scraper(name=data['name'], target_url=data['target_url'], 
                          data_to_scrape=data['data_to_scrape'], 
                          additional_params=data['additional_params'])
    db.session.add(new_scraper)
    db.session.commit()
    return jsonify({'message': 'Scraper designed successfully'}), 201

@scrapers_blueprint.route('/design', methods=['GET'])
@jwt_required
def get_all_scrapers():
    scrapers = Scraper.query.all()
    output = []
    for scraper in scrapers:
        scraper_data = {'name': scraper.name, 'target_url': scraper.target_url, 
                        'data_to_scrape': scraper.data_to_scrape, 
                        'additional_params': scraper.additional_params}
        output.append(scraper_data)
    return jsonify({'scrapers': output})

@scrapers_blueprint.route('/design/<scraper_id>', methods=['GET'])
@jwt_required
def get_one_scraper(scraper_id):
    scraper = Scraper.query.filter_by(id=scraper_id).first()
    if not scraper:
        return jsonify({'message': 'No scraper found!'})
    scraper_data = {'name': scraper.name, 'target_url': scraper.target_url, 
                    'data_to_scrape': scraper.data_to_scrape, 
                    'additional_params': scraper.additional_params}
    return jsonify({'scraper': scraper_data})

@scrapers_blueprint.route('/design/<scraper_id>', methods=['PUT'])
@jwt_required
def update_scraper(scraper_id):
    data = request.get_json()
    scraper = Scraper.query.filter_by(id=scraper_id).first()
    if not scraper:
        return jsonify({'message': 'No scraper found!'})
    scraper.name = data['name']
    scraper.target_url = data['target_url']
    scraper.data_to_scrape = data['data_to_scrape']
    scraper.additional_params = data['additional_params']
    db.session.commit()
    return jsonify({'message': 'Scraper updated successfully'})

@scrapers_blueprint.route('/design/<scraper_id>', methods=['DELETE'])
@jwt_required
def delete_scraper(scraper_id):
    scraper = Scraper.query.filter_by(id=scraper_id).first()
    if not scraper:
        return jsonify({'message': 'No scraper found!'})
    db.session.delete(scraper)
    db.session.commit()
    return jsonify({'message': 'Scraper deleted successfully'})
```