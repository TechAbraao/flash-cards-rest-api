from flask import Blueprint, request, jsonify
from src.app.controllers.cards_controller import CardsController

cards = Blueprint('cards', __name__, url_prefix='/api')
controller = CardsController()

@cards.route('/decks/<string:deck_id>/cards', methods=['POST'])
def add_flashcard(): pass

@cards.route('/decks/<string:deck_id>/cards/random', methods=['GET'])
def get_random_flashcard(deck_id): pass

@cards.route('/cards/<string:card_id>', methods=['GET'])
def get_cards(card_id): pass    

@cards.route('/cards/<string:card_id>', methods=['PUT'])
def update_card(card_id): pass

@cards.route('/cards/<int:card_id>', methods=['DELETE'])
def delete_card(card_id): pass