from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class Hypothesis(Base):
    __tablename__ = "hypotheses"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String(500), nullable=False)
    result = Column(Text, nullable=False)
