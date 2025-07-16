from flask import Flask

from src.app.blueprints.api.decks import decks
from src.app.blueprints.api.flashcards import flashcards
from src.app.settings.database.init_db import init_db

def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")
    
    app.register_blueprint(decks)
    app.register_blueprint(flashcards)  
    
    return app

app = create_app()

if __name__ == "__main__":
    init_db()
    app.run()
