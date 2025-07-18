from src.app.settings.database.databases import SessionLocal
from src.app.models.decks_model import Deck
from uuid import uuid4
from datetime import datetime
from src.app.utils.decorators.decorators import handle_db_errors

class DecksServices:
    def __init__(self):
        self.session = SessionLocal()
    
    @handle_db_errors
    def get_all_decks(self):
        decks = self.session.query(Deck).all()
        return [deck.to_dict() for deck in decks] if decks else []

    @handle_db_errors
    def get_deck_by_id(self, id, type_object=None): 
        deck = self.session.query(Deck).filter(Deck.id == id).first()
        if type_object == "orm":
            return deck
        return deck.to_dict()

    @handle_db_errors
    def add_deck(self, data_deck):
        new_deck = Deck(
            id=uuid4(),
            title=data_deck['title'],
            description=data_deck.get('description'),
            tags=data_deck.get('tags', []),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.session.add(new_deck)
        self.session.commit()
        self.session.refresh(new_deck) 
        return new_deck.to_dict()
        
    @handle_db_errors
    def update_deck(self, id, data_deck):
        deck = self.get_deck_by_id(id, type_object="orm")
        if not deck:
            return None
        
        if "title" in data_deck:
            deck.title = data_deck.get("title")

        if "description" in data_deck:
            deck.description = data_deck.get("description")

        if "tags" in data_deck:
            deck.tags = data_deck.get("tags")
        
        try:
            self.session.commit()
            return deck.to_dict()
        except Exception as e:
            self.session.rollback()
            raise e

decks_services = DecksServices()
