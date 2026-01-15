import asyncio
from voice_assistant.listener import listen_microphone
from voice_assistant.stt_whisper import speech_to_text
from voice_assistant.tts_edge import speak
import httpx


async def main():
    print("Jarvis Voice Assistant is running...")

    while True:
        audio_path = listen_microphone()
        if not audio_path:
            continue

        print("Распознаю речь...")
        text = speech_to_text(audio_path)
        print(f"Вы сказали: {text}")

        async with httpx.AsyncClient() as client:
            r = await client.post(
                "http://localhost:8000/analyze",
                json={"query": text}
            )
            result = r.json().get("result")

        print("Ответ ассистента:")
        print(result)

        speak(result)


if __name__ == "__main__":
    asyncio.run(main())
