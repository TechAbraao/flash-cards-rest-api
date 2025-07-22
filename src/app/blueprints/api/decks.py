from flask import Blueprint, request
from src.app.controllers.decks_controller import DecksController
from src.app.schemas.decks_schema import request_decks_schema, request_deck_id_schema
from src.app.services.decks_services import decks_services
from ..constants.routes import DECKS as routes

decks = Blueprint('decks', __name__)
controller = DecksController(
    request_validator=request_decks_schema, 
    deck_services=decks_services,
    id_validator=request_deck_id_schema
)
routes = routes.get("get_all_decks")
@decks.route(routes.get("URI"), methods=[routes.get("method")])
def get_all_decks(): 
    return controller.get_all_decks()

@decks.route(routes.get("URI"), methods=[routes.get("method")])
def create_deck(): 
    return controller.create_deck(request.get_json())

@decks.route(routes.get("URI"), methods=[routes.get("method")])
def get_deck(deck_id): 
    return controller.get_deck_by_id(deck_id)

@decks.route(routes.get("URI"), methods=[routes.get("method")])
def update_deck(deck_id): 
    return controller.change_existing_deck(request.get_json(), deck_id)

@decks.route(routes.get("URI"), methods=[routes.get("method")])
def delete_deck(deck_id): 
    return controller.delete_existing_deck(deck_id)
