from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.tg_bot_webhook.bot.messages.base import BaseMessage


class StartMessage(BaseMessage):
    text = "👋 Привет! Тестируем"
    reply = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1️⃣ Тест", callback_data="None")],
            [InlineKeyboardButton(text="2️⃣ Test", url="https://ya.ru")],
        ],
    )
