from src.app.utils.responses.response import APIResponse
from werkzeug.exceptions import BadRequest, NotFound
from marshmallow import ValidationError
from src.app.schemas.decks_schema import RequestDecksSchema, RequestDeckIdSchema
from src.app.services.decks_services import DecksServices
from src.app.validators.deck_validator import DeckValidator

class DecksController:
    def __init__(self):
        self.request_validator = RequestDecksSchema()
        self.id_validator = RequestDeckIdSchema()
        self.deck_services = DecksServices()
        self.deck_validator = DeckValidator()
    
    def get_all_decks(self):
        decks = self.deck_services.get_all_decks()
        
        if not decks: 
            return ( APIResponse.error(message="Nenhum deck encontrado. Retornando dados mock.", data=decks, status_code=200) )
        
        return ( APIResponse.success(message="Listagem de decks retornada com sucesso.", data=decks,status_code=200) )
    
    def get_deck_by_id(self, id):
        is_uuid, error_or_uuid = self.deck_validator.check_uuid(id)
        if not is_uuid:
            return APIResponse.error(message="Erro na validação.", error=error_or_uuid, status_code=BadRequest.code)
        
        uuid_exists_or_no = self.deck_services.check_exists_uuid(id)
        if not uuid_exists_or_no:
            return APIResponse.error(message="UUID inexistente na base de dados.", error="Não achou", status_code=NotFound.code)
        
        find_deck = self.deck_services.get_deck_by_id(id)
        return APIResponse.success(message="Deck encontrado com sucesso.", data=find_deck, status_code=200)
        
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
