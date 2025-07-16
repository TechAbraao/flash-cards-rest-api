from src.app.utils.responses.response import APIResponse
from src.app.utils.mocks.decks_mocks import mocks_responses_decks as mock
from werkzeug.exceptions import BadRequest
from marshmallow import ValidationError

class DecksController:
    def __init__(self, request_validator, deck_services):
        self.request_validator = request_validator
        self.deck_services = deck_services
    
    def get_all_decks(self):
        decks = self.deck_services.get_all_decks()
        if not decks:
            return APIResponse.error(
            message="Nenhum deck encontrado. Retornando dados mock.",
            data=mock["mock_get_decks"],
            status_code=200
        )
        return APIResponse.success(
            message="Listagem de decks retornada com sucesso.", 
            data=decks,
            status_code=200
        )

    def create_deck(self, data):
        try:
            deck_validated = self.request_validator.load(data)
        except ValidationError as err:
            return APIResponse.error(
                message="Erro de validação.",
                error=err.messages,
                status_code=BadRequest.code
            )
        
        self.deck_services.add_deck(data)
        data_json = self.request_validator.dump(data)
        return APIResponse.success(
            message="Deck criado com sucesso.",
            data=data_json,
            status_code=201
        )
        
        