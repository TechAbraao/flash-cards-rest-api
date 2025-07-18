from src.app.utils.responses.response import APIResponse
from src.app.utils.mocks.decks_mocks import mocks_responses_decks as mock
from werkzeug.exceptions import BadRequest
from marshmallow import ValidationError

class DecksController:
    def __init__(self, request_validator, deck_services, id_validator):
        self.request_validator = request_validator
        self.id_validator = id_validator
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
    
    def get_deck_by_id(self, id): 
        try:
            id_validated = self.id_validator.load({"id": id})
        except ValidationError as err:
            return APIResponse.error(
                message="Erro na validação.",
                error=err.messages,
                status_code=BadRequest.code
            )
        
        find_deck = self.deck_services.get_deck_by_id(id)
        return APIResponse.success(
            message="Deck encontrado com sucesso.",
            data=find_deck,
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
        
    def change_existing_deck(self, data, id): 
        try:
            id_validated = self.id_validator.load({"id": id})
        except ValidationError as err:
            return APIResponse.error(
                message="Erro na validação do campo UUID.",
                error=err.messages,
                status_code=BadRequest.code
            )
        if not data:
            return {"error": "Corpo JSON inválido ou ausente"}, 400
        
        data_model = self.request_validator.load(data)
        self.deck_services.update_deck(id, data_model)
        return APIResponse.success(
            message="Deck atualizado com sucesso.",
            status_code=200,
            data=data
        )
