from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.get_all_teams_controller import GetAllTeamController

class GetAllTeamsViews:
    def search_all_teams(self) -> HttpResponse:
        get_all_teams = GetAllTeamController()

        formatted_response = get_all_teams.search_all_teams()

        return HttpResponse(status_code=200,body=formatted_response) 