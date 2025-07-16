from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_name: str = "flashcards"
DATABASE_URL: str = f"postgresql+psycopg2://postgres:postgres@localhost:5432/{db_name}"

engine = create_engine(DATABASE_URL, echo=True,pool_recycle=3600) # Create the database engine with connection pooling

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Session factory for creating new sessions

Base = declarative_base() # Base class for declarative models
