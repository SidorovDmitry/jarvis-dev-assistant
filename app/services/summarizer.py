def summarize_results(query: str, sources: dict):
    """
    Сравнивает источники и формирует итоговый вывод.
    """

    text = f"Гипотеза: {query}\n\n"
    text += "Сравнение источников:\n"

    for name, content in sources.items():
        text += f"- {name}: {content}\n"

    text += "\nВывод: информация собрана и обработана."
    return text
