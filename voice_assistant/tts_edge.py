import asyncio
import edge_tts
import uuid


VOICE = "ru-RU-DmitryNeural"  # мужской голос, стиль «джарвис»


def speak(text: str):
    """
    Озвучка текста через Edge‑TTS.
    """
    filename = f"tts_{uuid.uuid4()}.mp3"

    async def _run():
        tts = edge_tts.Communicate(text, VOICE)
        await tts.save(filename)

    asyncio.run(_run())

    # Воспроизведение
    import playsound
    playsound.playsound(filename)
