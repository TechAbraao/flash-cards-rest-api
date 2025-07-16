from src.app.settings.database.databases import Base, engine
from src.app.models.decks import Deck
from src.app.models.flashcards import Flashcard

def init_db():
    Base.metadata.create_all(bind=engine)
