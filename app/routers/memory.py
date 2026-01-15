from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.memory import add_note, get_all_notes
from app.dependencies import get_db

router = APIRouter()

class NoteRequest(BaseModel):
    text: str


@router.post("/add")
def add(req: NoteRequest, db=Depends(get_db)):
    add_note(req.text, db)
    return {"status": "saved"}


@router.get("/all")
def get_all(db=Depends(get_db)):
    notes = get_all_notes(db)
    return {"notes": notes}
