from src.app.utils.responses.response import APIResponse
from werkzeug.exceptions import BadRequest, NotFound
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
        
        verify_id_exists = self.service.verify_deck_id_exists(uuid_value)
        if not verify_id_exists:
            return APIResponse.error(
                message="Deck não encontrado.",
                error="ID inexistente na base de dados.",
                status_code=NotFound.code
                )
            
        cards, deck_name = self.service.get_cards_by_deck_id(uuid_value)
        
        return APIResponse.success(
            message=f"Cards encontrados com sucesso.",
            data={
                    "deckName": deck_name,
                    "cards": cards,
                },
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
    
    def searching_specific_card(self, id):
        is_uuid, uuid_value = self.validator.check_uuid(id)
        if not is_uuid:
            return APIResponse.error(
                message="UUID Inválido.",
                error="Formato do UUID não é válido.",
                status_code=BadRequest.code
            )
        verify_id_exists = self.service.verify_card_id_exists(id)
        if not verify_id_exists:
            return APIResponse.error(
                message="ID inexistente na base de dados.",
                status_code=NotFound.code,
                error="Nenhum dado encontrado."
            )
            
        card = self.service.get_card_by_id(uuid_value)
        
        return APIResponse.success(
            message="Detalhes do card encontrado com sucesso.",
            status_code=200,
            data=card,
        )