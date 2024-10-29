from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.tg_bot_webhook.bot.messages.base import BaseMessage


class StartMessage(BaseMessage):
    text = "👋 Привет! Тестируем"
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Тест", callback_data="start")],
        ],
    )
