from flask import Blueprint, request
from src.app.controllers.cards_controller import CardsController

cards = Blueprint('cards', __name__, url_prefix='/api')
controller = CardsController()

@cards.route('/decks/<string:deck_uuid>/cards', methods=['POST'])
def add_card_at_deck(deck_uuid): 
    return controller.post_cards_by_deck(deck_uuid, request.get_json())

@cards.route('/decks/<string:deck_uuid>/cards', methods=['GET'])
def get_cards_by_deck(deck_uuid): 
    return controller.get_cards_by_deck(deck_uuid)

# Implementação pro futuro.
@cards.route('/decks/<string:deck_uuid>/cards/random', methods=['GET'])
def get_random_card(deck_uuid): pass

@cards.route('/cards/<string:card_uuid>', methods=['GET'])
def get_cards(card_uuid): return controller.searching_specific_card(card_uuid)

@cards.route('/cards/<string:card_uuid>', methods=['PUT'])
def update_card(card_uuid): return controller.update_card(card_uuid, request.get_json())

@cards.route('/cards/<string:card_uuid>', methods=['DELETE'])
def delete_card(card_uuid): return controller.delete_card(card_uuid)