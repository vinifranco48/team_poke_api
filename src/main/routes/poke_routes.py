from flask import Blueprint, jsonify, request

poke_routes_bp = Blueprint('poke_routes', __name__)

@poke_routes_bp.route('/api/teams', methods={'GET'})
def get_all_teams():
    return jsonify({
        'resp':'ok'
    })

@poke_routes_bp.route('/api/teams/<int:user>', methods={'GET'})
def get_team(user: int):

    print(user)
    return jsonify({
        'resp':'ok'
    })

@poke_routes_bp.route('/api/teams', methods={'POST'})
def register_team():
    print(request.json)
    return jsonify({
        'resp':'ok'
    })

