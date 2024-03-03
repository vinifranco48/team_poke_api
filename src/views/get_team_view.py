from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.get_team_controller import GetTeamController

class GetTeamView:
    def search_team(self, http_request: HttpRequest) -> HttpResponse:
        get_team = GetTeamController()

        params = http_request.query_params
        id = params["id"]
        formatted_response = get_team.search_team_id(id)

        return HttpResponse(status_code=200,body=formatted_response) 