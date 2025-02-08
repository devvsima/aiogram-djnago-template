from aiogram import BaseMiddleware
from aiogram.types import Message

from app.settings import tg_settings
from tgbot.database.services.users import get_user


from typing import Any, Callable


class AdminMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, message: Message, data: dict) -> Any:
        if user := await get_user(message.from_user.id):
            if user.id in tg_settings:
                data["user"] = user
                return await handler(message, data)
        return
