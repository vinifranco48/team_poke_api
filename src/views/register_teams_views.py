from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.register_teams_controller import RegisterTeamsController

class RegisterTeamsViews:
    def search_and_register(self, http_request: HttpRequest) -> HttpResponse:
        register_teams_controller = RegisterTeamsController()
        
        body = http_request.body
        user, team = body["user"], body["team"]

        formatted_response = register_teams_controller.search_and_register(user, team)

        return HttpResponse(status_code=200,body=formatted_response) 

