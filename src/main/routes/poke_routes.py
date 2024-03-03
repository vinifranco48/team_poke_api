from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.views.register_teams_views import RegisterTeamsViews

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
    register_teams_views = RegisterTeamsViews()
    print(request.json)
    http_request = HttpRequest(body=request.json)
    http_response =  register_teams_views.search_and_register(http_request)
    return jsonify(http_response.body), http_response.status_code

