from fastapi import APIRouter
from app.config import settings
import os

router = APIRouter()

@router.get("/local")
def list_local_projects():
    base = settings.PROJECTS_PATH
    if not os.path.exists(base):
        return {"error": f"Path not found: {base}"}

    dirs = [d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))]
    return {"projects": dirs}


@router.get("/github")
def github_info(repo: str):
    return {"repo": repo, "status": "ready for analysis"}
