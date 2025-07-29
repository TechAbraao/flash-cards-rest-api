from marshmallow import ValidationError
from src.app.schemas.cards_schema import RequestCardSchema

class CardsValidator(): 
    def __init__(self, uuid_request_schema):
        self.uuid_request_schema = uuid_request_schema
        self.body_request_schema = RequestCardSchema()
        
    def check_uuid(self, uuid):
        try:
            uuid_validated = self.uuid_request_schema.load({"id": uuid})
            return True, uuid_validated["id"]
        except ValidationError as err:
            return False, None
    
    def check_body_card(self, body):
        try:
            validated_body = self.body_request_schema.load(body)
            return True, validated_body
        except ValidationError as err:
            return False, err.messages