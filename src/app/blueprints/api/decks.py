from flask import Blueprint, request
from src.app.controllers.decks_controller import DecksController
from src.app.schemas.docks_schema import request_decks_schema, request_deck_id_schema
from src.app.services.decks_services import decks_services

decks = Blueprint('decks', __name__, url_prefix='/api/')
deck_controller = DecksController(
    request_validator=request_decks_schema, 
    deck_services=decks_services,
    id_validator=request_deck_id_schema
)

@decks.route('/decks', methods=['GET'])
def get_all_decks(): return deck_controller.get_all_decks()

@decks.route('/decks', methods=['POST'])
def create_deck(): return deck_controller.create_deck(request.get_json())

@decks.route('/decks/<string:deck_id>', methods=['GET'])
def get_deck(deck_id): return deck_controller.get_deck_by_id(deck_id)

@decks.route('/decks/<int:deck_id>', methods=['PUT'])
def update_deck(deck_id): pass