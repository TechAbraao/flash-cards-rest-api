from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class ApplicationSetting:
    FLASK_APP: str = os.getenv("FLASK_APP", "app:create_app")
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG: int = int(os.getenv("FLASK_DEBUG", "0"))
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", "5432"))
    DATABASE_USER: str = os.getenv("DATABASE_USER", "user")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "password")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "flash_cards_db")
    
configs = ApplicationSetting()
