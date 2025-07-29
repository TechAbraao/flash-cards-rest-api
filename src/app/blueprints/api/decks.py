from flask import Blueprint, request
from src.app.controllers.decks_controller import DecksController
from ..constants.routes import DECKS as r

decks = Blueprint('decks', __name__)
controller = DecksController()

@decks.route(r.get("get_all_decks").get("URI"), methods=[r.get("get_all_decks").get("method")])
def get_all_decks(): return controller.get_all_decks()

@decks.route(r.get("create_deck").get("URI"), methods=[r.get("create_deck").get("method")])
def create_deck(): return controller.create_deck(request.get_json())

@decks.route(r.get("get_deck").get("URI"), methods=[r.get("get_deck").get("method")])
def get_deck(deck_id): return controller.get_deck_by_id(deck_id)

@decks.route(r.get("update_deck").get("URI"), methods=[r.get("update_deck").get("method")])
def update_deck(deck_id): return controller.change_existing_deck(request.get_json(), deck_id)

@decks.route(r.get("delete_deck").get("URI"), methods=[r.get("delete_deck").get("method")])
def delete_deck(deck_id): return controller.delete_existing_deck(deck_id)
