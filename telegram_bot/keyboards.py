from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Анализ гипотезы")],
        [KeyboardButton(text="Показать заметки")]
    ],
    resize_keyboard=True
)
