from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.app.settings.application.application_settings import configs as c

try:
    DATABASE_URL: str = f"postgresql+psycopg2://{c.DATABASE_USER}:{c.DATABASE_PASSWORD}@{c.DATABASE_HOST}:{c.DATABASE_PORT}/{c.DATABASE_NAME}"
    engine = create_engine(DATABASE_URL, echo=False, pool_recycle=3600) # Create the database engine with connection pooling
    SessionLocal = sessionmaker(bind=engine) # Session factory for creating new sessions
    Base = declarative_base() # Base class for declarative models
except Exception as e:
    exit("Não foi possível conectar-se ao banco de dados.")