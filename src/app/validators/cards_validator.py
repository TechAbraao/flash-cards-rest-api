from marshmallow import ValidationError
from src.app.utils.responses.response import APIResponse
from werkzeug.exceptions import BadRequest

class CardsValidator(): 
    def __init__(self, uuid_request_schema):
        self.uuid_request_schema = uuid_request_schema
        
    def check_uuid(self, uuid):
        try:
            uuid_validated = self.uuid_request_schema.load({"id": uuid})
            return True, uuid_validated["id"]
        except ValidationError as err:
            return False, None
    
    def check_body_card(self, body):
        return body