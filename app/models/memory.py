from sqlalchemy import Column, Integer, Text
from app.db import Base

class MemoryNote(Base):
    __tablename__ = "memory_notes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
