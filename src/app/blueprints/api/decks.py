from flask import Blueprint, request
from src.app.controllers.decks_controller import DecksController
from src.app.schemas.docks_schema import request_decks_schema 
from src.app.services.decks_services import decks_services

decks = Blueprint('decks', __name__, url_prefix='/api/')
responses = DecksController(
    request_validator=request_decks_schema, 
    deck_services=decks_services
)

@decks.route('/decks', methods=['GET'])
def get_all_decks(): return responses.get_all_decks()

@decks.route('/decks', methods=['POST'])
def create_deck(): 
    data = request.get_json()
    return responses.create_deck(data)

@decks.route('/decks/<int:deck_id>', methods=['GET'])
def get_deck(deck_id): pass

@decks.route('/decks/<int:deck_id>', methods=['PUT'])
def update_deck(deck_id): pass