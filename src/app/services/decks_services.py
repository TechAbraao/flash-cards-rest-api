from src.app.settings.database.databases import SessionLocal
from src.app.models.decks_model import Deck
from uuid import uuid4
from datetime import datetime

class DecksServices:
    def __init__(self):
        self.session = SessionLocal()
    
    def get_all_decks(self):
        decks = self.session.query(Deck).all()
        return [deck.to_dict() for deck in decks] if decks else []

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
            


decks_services = DecksServices()
