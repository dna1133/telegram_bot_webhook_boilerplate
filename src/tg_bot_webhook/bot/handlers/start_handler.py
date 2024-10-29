import logging

from aiogram import types

from src.tg_bot_webhook.bot.messages.start import StartMessage

logger = logging.getLogger(__name__)


async def start_handler(message: types.Message) -> None:
    content = StartMessage().message()
    await message.answer(text="test text", parse_mode=str)
    # await message.answer(**content)
