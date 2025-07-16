from src.app.settings.database.databases import Base
from sqlalchemy import Column, String, DateTime, ARRAY, UUID, ForeignKey
from sqlalchemy.orm import relationship

class Flashcard(Base):
    __tablename__ = 'flashcards'

    id = Column(UUID, primary_key=True, unique=True, nullable=False)
    question = Column(String(30), nullable=False)
    answer = Column(String(300), nullable=False)
    tags = Column(ARRAY(String), nullable=True)
    deck_id = Column(UUID, ForeignKey('decks.id', ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    deck = relationship("Deck", back_populates="flashcards")  # Relacionamento reverso - cada flashcard pertence a um deck

    def __repr__(self):
        return f"<Flashcard(id={self.id}, question={self.question}, answer={self.answer})>"
