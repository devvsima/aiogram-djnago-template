from typing import Any, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.settings import tgbot
from tgbot.database.services.users import get_user


class AdminMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, message: Message, data: dict) -> Any:
        if user := await get_user(message.from_user.id):
            if user.id in tgbot.ADMINS:
                data["user"] = user
                return await handler(message, data)
        return
