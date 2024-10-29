from aiohttp import web
import asyncio
import logging

from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from src.tg_bot_webhook.core.configs import settings

# from tg_bot_webhook.bot.handlers.start_handler import start_handler
from src.tg_bot_webhook.core.aiogr.middlewares import UserMiddleware
from src.tg_bot_webhook.bot.handlers.start_handler import start_handler

router = Router()


def add_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.message.middleware(UserMiddleware())
    dispatcher.callback_query.middleware(UserMiddleware())


def add_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.message.register(start_handler, Command("start"))
    dispatcher.callback_query.register(start_handler, F.data == "start")


async def init_bot() -> web.Application:
    logging.basicConfig(level=settings.LOGGING_LEVEL)
    dp = Dispatcher()
    add_middlewares(dp)

    add_handlers(dp)

    bot = Bot(
        token=settings.TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await bot.set_webhook(settings.TELEGRAM_WEB_HOOK)
    app = web.Application()
    setup_application(app, dp, bot=bot)
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=settings.TELEGRAM_WEBHOOK_PATH)
    return app


def start_bot(app):
    web.run_app(app, host=settings.TELEGRAM_HOST, port=settings.TELEGRAM_PORT)


if __name__ == "__main__":
    start_bot(init_bot())
