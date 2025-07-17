from functools import wraps
from src.app.exceptions.database_connection_error import DatabaseConnectionError
from sqlalchemy.exc import OperationalError

def handle_db_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError as e:
            raise DatabaseConnectionError(original_exception=e) from e
    return wrapper