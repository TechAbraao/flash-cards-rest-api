class DatabaseConnectionError(Exception):
    def __init__(self, message="Erro ao estabelecer uma conexão com o banco de dados.", original_exception=None):
        super().__init__(message)
        self.message = message
        self.original_exception = original_exception
