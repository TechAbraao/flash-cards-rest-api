from src.app import app
from flask import jsonify
from sqlalchemy.exc import OperationalError

@app.errorhandler(OperationalError)
def handle_db_error(e):
    return jsonify({"error": "Erro de conexão com o banco de dados, tente mais tarde."}), 503
