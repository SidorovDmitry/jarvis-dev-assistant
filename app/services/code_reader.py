import os
import httpx
from app.config import settings


def analyze_code(local_path: str | None, github_repo: str | None, db):
    """
    Анализ кода:
    - локальная директория
    - GitHub репозиторий
    """

    if local_path:
        return analyze_local_project(local_path)

    if github_repo:
        return analyze_github_repo(github_repo)

    return "Не указан путь или GitHub репозиторий."


def analyze_local_project(path: str):
    if not os.path.exists(path):
        return f"Путь не найден: {path}"

    files = []
    for root, _, filenames in os.walk(path):
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(root, f))

    return {
        "project_path": path,
        "python_files": files,
        "summary": f"Найдено {len(files)} Python файлов."
    }


def analyze_github_repo(repo_url: str):
    """
    Пример: https://github.com/user/project
    """

    api_url = repo_url.replace("https://github.com/", "https://api.github.com/repos/")

    headers = {"Authorization": f"token {settings.GITHUB_TOKEN}"} if settings.GITHUB_TOKEN else {}

    r = httpx.get(api_url, headers=headers)

    if r.status_code != 200:
        return f"Ошибка GitHub API: {r.text}"

    data = r.json()

    return {
        "repo": repo_url,
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "description": data.get("description"),
        "summary": "GitHub репозиторий успешно проанализирован."
    }
