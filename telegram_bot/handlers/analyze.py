from aiogram.types import Message
import httpx

async def analyze_handler(message: Message):
    text = message.text or ""

    if message.voice:
        file_id = message.voice.file_id
        await message.answer("Голосовое сообщение получено. Распознаю...")

        # Получение файла
        file = await message.bot.get_file(file_id)
        file_path = file.file_path
        file_url = f"https://api.telegram.org/file/bot{message.bot.token}/{file_path}"

        # Отправка в Whisper API FastAPI
        async with httpx.AsyncClient() as client:
            r = await client.post(
                "http://api:8000/analyze",
                json={"query": f"VOICE: {file_url}"}
            )
            result = r.json().get("result")

        await message.answer(result)
        return

    # Текстовый анализ
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://api:8000/analyze",
            json={"query": text}
        )
        result = r.json().get("result")

    await message.answer(result)
