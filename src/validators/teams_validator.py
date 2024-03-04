from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.validators.request_json_validator import request_json_validator

def teams_validator(request: any) -> None:
    request_json_validator(request)

    body_validator = Validator({
        "user": {"type": "string", "required": True, "empty": False},
        "team": {"type": "list", "minlength": 1, "required": True, "schema": {"type": "string"}}
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
