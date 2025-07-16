from src.app.settings.database.databases import Base, engine
from src.app.models.decks_model import Deck
from src.app.models.flashcards_model import Flashcard

def init_db():
    Base.metadata.create_all(bind=engine)
