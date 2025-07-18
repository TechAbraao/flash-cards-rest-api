from src.app.settings.database.databases import Base
from sqlalchemy import Column, String, DateTime, ARRAY, UUID, ForeignKey
from sqlalchemy.orm import relationship

class Deck(Base):
    __tablename__ = 'decks'

    id = Column(UUID, primary_key=True, unique=True, nullable=False)
    title = Column(String(40), nullable=False)
    description = Column(String(500), nullable=True)
    tags = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    flashcards = relationship("Flashcard", back_populates="deck", cascade="all, delete-orphan")  # Relacionamento - um deck tem várias flashcards

    def __repr__(self):
        return f"<Deck(id={self.id}, title={self.title}, description={self.description})>"
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'tags': self.tags,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'flashcards': [flashcard.to_dict() for flashcard in self.flashcards] if self.flashcards else []
        }
