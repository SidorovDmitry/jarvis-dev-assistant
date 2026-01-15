from app.models.memory import MemoryNote
from app.models.hypothesis import Hypothesis


def add_note(text: str, db):
    note = MemoryNote(text=text)
    db.add(note)
    db.commit()


def get_all_notes(db):
    return db.query(MemoryNote).all()


def save_hypothesis(query: str, result: str, db):
    hyp = Hypothesis(query=query, result=result)
    db.add(hyp)
    db.commit()
