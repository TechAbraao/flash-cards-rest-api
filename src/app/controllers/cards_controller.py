from src.app.utils.responses.response import APIResponse
from werkzeug.exceptions import BadRequest
from src.app.utils.mocks.decks_mocks import mocks_responses_decks as mock
from src.app.services.cards_services import CardsService
from src.app.validators.cards_validator import CardsValidator
from src.app.schemas.decks_schema import request_deck_id_schema

class CardsController:
    def __init__(self):
        self.service = CardsService()
        self.validator = CardsValidator(uuid_request_schema=request_deck_id_schema)
    
    def get_cards_by_deck(self, id):
        is_uuid, uuid_value = self.validator.check_uuid(id)
        if not is_uuid:
            return APIResponse.error(
                message="UUID Inválido.",
                error="Formato do UUID não é válido.",
                status_code=BadRequest.code
            )
            
        cards = self.service.get_cards_by_deck_id(uuid_value)
        return APIResponse.success(
            message="Cards encontrados com sucesso.",
            data=cards,
            status_code=200
        )       
        
    def post_cards_by_deck(self, id, body): 
        is_uuid, uuid_value = self.validator.check_uuid(id)
        if not is_uuid:
            return APIResponse.error(
                message="UUID Inválido.",
                error="Formato do UUID não é válido.",
                status_code=BadRequest.code
            )
        
        card_added = self.service.post_cards_by_deck_id(uuid_value, body)
        
        return APIResponse.success(
            message="Sucesso ao cadastrar Card.",
            status_code=201,
            data=card_added.to_dict()
        )
  