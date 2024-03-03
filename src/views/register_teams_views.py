from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class RegisterTeamsViews:
    def search_and_register(self, http_request: HttpRequest):
        return HttpResponse(status_code=200,body={'resp':'ok'}) 
