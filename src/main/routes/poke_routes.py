from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.views.register_teams_view import RegisterTeamsView
from src.views.get_all_teams_view import GetAllTeamsView
from src.views.get_team_view import GetTeamView
from src.errors.error_hendler import error_hendler
from src.validators.teams_validator import teams_validator


poke_routes_bp = Blueprint('poke_routes', __name__)

@poke_routes_bp.route('/api/teams', methods={'GET'})
def get_all_teams():
    http_response = None
    try:
        get_all_teams = GetAllTeamsView()

        http_response =  get_all_teams.search_all_teams()

    except Exception as exception:
        http_response = error_hendler(exception)
        
    return jsonify(http_response.body), http_response.status_code


@poke_routes_bp.route('/api/teams/<int:user>', methods={'GET'})
def get_team(user: int):
    http_response = None
    try:
        get_team = GetTeamView()
        
        http_request = HttpRequest(query_params={"id": user})
        http_response =  get_team.search_team(http_request)

    except Exception as exception:
        http_response = error_hendler(exception)

    return jsonify(http_response.body), http_response.status_code

@poke_routes_bp.route('/api/teams', methods={'POST'})
def register_team():
    http_response = None
    try:
        teams_validator(request)
        register_teams_views = RegisterTeamsView()

        http_request = HttpRequest(body=request.json)
        http_response =  register_teams_views.search_and_register(http_request)
        
    except Exception as exception:
        http_response = error_hendler(exception)

    return jsonify(http_response.body), http_response.status_code
