import whisper

model = whisper.load_model("base")


def speech_to_text(audio_path: str) -> str:
    """
    Распознавание речи через Whisper.
    """
    try:
        result = model.transcribe(audio_path, language="ru")
        return result["text"]
    except Exception as e:
        return f"Ошибка распознавания: {e}"
