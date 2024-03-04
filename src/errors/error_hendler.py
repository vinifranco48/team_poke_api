from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.errors.error_types.http_not_found import HttpNotFoundError

def error_hendler(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": {
                    "title": error.name,
                    "details": error.message
                }
            }
        )
    
    if isinstance(error, HttpBadRequestError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": {
                    "title": error.name,
                    "details": error.message
                }
            }
        )
    
    if isinstance(error, HttpNotFoundError):
        return HttpResponse(
            status_code = error.status_code,
            body={
                "errors": {
                    "title": error.name,
                    "details": error.message
                }
            }
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "errors": {
                "title": "Server Error",
                "details": str(error)
            }
        }
    )


    
