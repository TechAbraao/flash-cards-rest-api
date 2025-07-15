from flask import Blueprint, request, jsonify

flashcards = Blueprint('flashcards', __name__, url_prefix='/api')

@flashcards.route('/decks/<deck_id>/cards', methods=['POST'])
def add_flashcard(): pass

@flashcards.route('/decks/<deck_id>/cards/random', methods=['GET'])
def get_random_flashcard(deck_id): pass

@flashcards.route('/cards/<int:card_id>', methods=['GET'])
def get_flashcard(card_id): pass    

@flashcards.route('/cards/<int:card_id>', methods=['PUT'])
def update_flashcard(card_id): pass

@flashcards.route('/cards/<int:card_id>', methods=['DELETE'])
def delete_flashcard(card_id): pass