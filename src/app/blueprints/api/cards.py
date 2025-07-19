from flask import Blueprint
from src.app.controllers.cards_controller import CardsController
from src.app.services.cards_services import CardsService
from src.app.validators.cards_validator import CardsValidator

cards = Blueprint('cards', __name__, url_prefix='/api')
controller = CardsController(service = CardsService(), validator = CardsValidator())

@cards.route('/decks/<string:deck_uuid>/cards', methods=['GET'])
def get_cards_by_deck(deck_uuid): return controller.get_cards_by_deck(deck_uuid)

@cards.route('/decks/<string:deck_uuid>/cards', methods=['POST'])
def add_card_at_deck(): pass

@cards.route('/decks/<string:deck_uuid>/cards/random', methods=['GET'])
def get_random_card(deck_uuid): pass

@cards.route('/cards/<string:card_uuid>', methods=['GET'])
def get_cards(deck_uuid): pass    

@cards.route('/cards/<string:card_uuid>', methods=['PUT'])
def update_card(deck_uuid): pass

@cards.route('/cards/<int:card_uuid>', methods=['DELETE'])
def delete_card(deck_uuid): pass