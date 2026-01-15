from app.services.searcher import search_sources
from app.services.summarizer import summarize_results
from app.services.memory import save_hypothesis


def analyze_hypothesis(query: str, db):
    """
    Основной процесс анализа гипотезы:
    1. Сбор информации из разных источников
    2. Сравнение и сводка
    3. Сохранение результата в БД
    """

    sources = search_sources(query)
    summary = summarize_results(query, sources)

    save_hypothesis(query, summary, db)

    return summary
