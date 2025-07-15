from flask import Blueprint, request, jsonify
from src.app.utils.responses.response import APIResponse

decks = Blueprint('decks', __name__, url_prefix='/api/')

@decks.route('/decks', methods=['GET'])
def get_decks():
    mock = [
        {
         'id': "UUID", 
         'title': 'Deck 1',
         'description': 'Description for Deck 1',
         'tags': ['tag1', 'tag2'],
         'created_at': '2023-10-01T12:00:00Z',
         'updated_at': '2023-10-01T12:00:00Z'
        }
    ]

    return APIResponse.success(
        message="Listagem de decks retornada com sucesso.", 
        data=mock,
        status_code=200
        )

@decks.route('/decks', methods=['POST'])
def create_deck(): pass

@decks.route('/decks/<int:deck_id>', methods=['GET'])
def get_deck(deck_id): pass

@decks.route('/decks/<int:deck_id>', methods=['PUT'])
def update_deck(deck_id): pass