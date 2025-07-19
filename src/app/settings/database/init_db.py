from src.app.settings.database.databases import Base, engine
from src.app.models.decks_model import Deck
from src.app.models.cards_model import Cards

def init_db():
    Base.metadata.create_all(bind=engine)
