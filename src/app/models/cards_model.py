from src.app.settings.database.databases import Base
from sqlalchemy import Column, String, DateTime, ARRAY, UUID, ForeignKey
from sqlalchemy.orm import relationship

class Cards(Base):
    __tablename__ = 'cards'

    id = Column(UUID, primary_key=True, unique=True, nullable=False)
    question = Column(String(30), nullable=False)
    answer = Column(String(300), nullable=False)
    tags = Column(ARRAY(String), nullable=True)
    deck_id = Column(UUID, ForeignKey('decks.id', ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    deck = relationship("Deck", back_populates="cards")

    def __repr__(self):
        return f"<Cards(id={self.id}, question={self.question}, answer={self.answer})>"

    def to_dict(self) -> dict: 
        return {
            "id" : str(self.id),
            "question" : self.question,
            "answer" : self.answer,
            "tags" : self.tags,
            "deck_id" : self.deck_id,
            "created_at" : self.created_at.isoformat() if self.created_at else None,
            "updated_at" : self.updated_at.isoformat() if self.updated_at else None
        }
    