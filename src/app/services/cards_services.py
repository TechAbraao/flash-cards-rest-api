from src.app.utils.decorators.decorators import handle_db_errors
from src.app.settings.database.databases import SessionLocal
from src.app.models.cards_model import Cards
from src.app.models.decks_model import Deck
from sqlalchemy.orm import joinedload
from uuid import uuid4
from datetime import datetime

class CardsService: 
   def __init__(self):
      self.session = SessionLocal()
   
   @handle_db_errors
   def post_cards_by_deck_id(self, uuid, body):
      deck = self.session.query(Deck).options(
         joinedload(Deck.cards)
      ).filter(Deck.id == uuid).first()
      
      if not deck:
         return None
      
      new_card = Cards(
        id=uuid4(),
        question=body.get('question'),
        answer=body.get('answer'),
        tags=body.get('tags'),
        deck_id=deck.id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
      )
      
      self.session.add(new_card)
      self.session.commit()
      self.session.refresh(new_card)
      return new_card
      
   @handle_db_errors
   def get_cards_by_deck_id(self, uuid):
      deck = self.session.query(Deck).options(
         joinedload(Deck.cards)
      ).filter(Deck.id == uuid).first()
      if not deck:
         return None, None
      deck_infos = deck.to_dict()
      return deck_infos.get("cards"), deck_infos.get("title")
   
   @handle_db_errors
   def verify_card_id_exists(self, id):
      result = self.session.query(Cards).filter(Cards.id == id).first()
      if not result:
         return False
      return True
      
   @handle_db_errors
   def verify_deck_id_exists(self, id):
    result = self.session.query(Deck).filter(Deck.id == id).first()
    return bool(result)   
      
   @handle_db_errors
   def get_card_by_id(self, card_id):
      finding_card = self.session.query(Cards).filter(Cards.id == card_id).first()
      if not finding_card:
         return None
      return finding_card.to_dict()