from fastapi import FastAPI
from app.routers import analyze, memory, projects

app = FastAPI(
    title="Jarvis Dev Assistant",
    description="Голосовой ассистент разработчика: анализ гипотез, сравнение источников, анализ кода",
    version="1.0.0"
)

app.include_router(analyze.router, prefix="/analyze", tags=["Analyze"])
app.include_router(memory.router, prefix="/memory", tags=["Memory"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])


@app.get("/")
def root():
    return {"status": "Jarvis Dev Assistant API is running"}
