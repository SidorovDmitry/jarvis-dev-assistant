from aiogram.types import Message
from telegram_bot.keyboards import main_kb

async def start_handler(message: Message):
    await message.answer(
        "Привет! Я Jarvis‑Dev Assistant.\n"
        "Отправь голосовое сообщение или текст — я проанализирую гипотезу.",
        reply_markup=main_kb
    )
