from typing import Any, Awaitable, Callable, Coroutine
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Coroutine[Any, Any, Any]:
        return await handler(event, data)
