import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")
    PROJECTS_PATH: str = os.getenv("PROJECTS_PATH", "C:/my_projects/")

settings = Settings()
