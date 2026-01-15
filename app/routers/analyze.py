from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.analyzer import analyze_hypothesis
from app.services.code_reader import analyze_code
from app.dependencies import get_db

router = APIRouter()

class HypothesisRequest(BaseModel):
    query: str

class CodeRequest(BaseModel):
    path: str | None = None
    github_repo: str | None = None


@router.post("/")
def analyze(req: HypothesisRequest, db=Depends(get_db)):
    result = analyze_hypothesis(req.query, db)
    return {"result": result}


@router.post("/code")
def analyze_code_route(req: CodeRequest, db=Depends(get_db)):
    result = analyze_code(req.path, req.github_repo, db)
    return {"result": result}
