from flask import Blueprint, jsonify, send_from_directory
import os

app_routes_bp = Blueprint('app_routes', __name__)

@app_routes_bp.route('/info', methods={'GET'})
def home():
    return jsonify({
        'name':'Poke Teams', 
        'description': 'A PokeAPI-based API for registering Pokémon teams, utilizing the PokeAPI to retrieve data related to the Pokémon creatures.',
        'version': '1.0v'
    })

@app_routes_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../static'), 'favicon.ico')

@app_routes_bp.route('/')
def swagger_ui():
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../templates'),
                          'docs.html')

@app_routes_bp.route('/openapi.json')
def swagger():
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../templates/documentation'),
                          'openapi.json')