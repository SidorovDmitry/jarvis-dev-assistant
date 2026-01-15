import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.config import settings
from telegram_bot.handlers.start import start_handler
from telegram_bot.handlers.analyze import analyze_handler
from telegram_bot.handlers.memory import memory_handler


async def main():
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())
    dp.message.register(analyze_handler)
    dp.message.register(memory_handler)

    print("Telegram bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
