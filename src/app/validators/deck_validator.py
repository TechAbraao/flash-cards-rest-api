from src.app.schemas.decks_schema import RequestDeckIdSchema
from marshmallow import ValidationError

class DeckValidator:
    def __init__(self):
        self.id_validator = RequestDeckIdSchema()
        
    def check_uuid(self, id):
        try:
            uuid_validated = self.id_validator.load({"id": id})
            return True, uuid_validated["id"]
        except ValidationError as err:
            return False, err.messages