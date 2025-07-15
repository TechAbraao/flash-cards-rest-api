from flask import Flask

from src.app.blueprints.api.decks import decks
from src.app.blueprints.api.flashcards import flashcards

def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")
    
    app.register_blueprint(decks)
    app.register_blueprint(flashcards)  
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run()
