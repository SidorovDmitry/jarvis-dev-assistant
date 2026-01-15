from aiogram.types import Message
import httpx

async def memory_handler(message: Message):
    if message.text == "Показать заметки":
        async with httpx.AsyncClient() as client:
            r = await client.get("http://api:8000/memory/all")
            notes = r.json().get("notes", [])

        if not notes:
            await message.answer("Заметок пока нет.")
            return

        text = "Ваши заметки:\n\n"
        for n in notes:
            text += f"- {n['text']}\n"

        await message.answer(text)
