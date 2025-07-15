from flask import Blueprint, request, jsonify

decks = Blueprint('decks', __name__, url_prefix='/api')

@decks.route('/decks', methods=['GET'])
def get_decks(): pass

@decks.route('/decks', methods=['POST'])
def create_deck(): pass

@decks.route('/decks/<int:deck_id>', methods=['GET'])
def get_deck(deck_id): pass

@decks.route('/decks/<int:deck_id>', methods=['PUT'])
def update_deck(deck_id): pass