from flask import Flask
from src.app.utils.responses.response import APIResponse
from src.app.exceptions.database_connection_error import DatabaseConnectionError
from src.app.blueprints.api.decks import decks
from src.app.blueprints.api.cards import cards
from src.app.settings.database.init_db import init_db

def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")
    app.register_blueprint(decks)
    app.register_blueprint(cards)  
    
    @app.errorhandler(DatabaseConnectionError)
    def handle_db_error(e):
        return APIResponse.error(
            message=e.message,
            error=str(e.original_exception),
            status_code=503
        )
    return app

app = create_app()

if __name__ == "__main__":
    init_db()
    app.run()
