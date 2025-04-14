from typing import Any, Callable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from tgbot.database.services.users import get_or_create_user


class UsersMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, event: Message | CallbackQuery, data: dict) -> Any:
        user = await get_or_create_user(
            user_id=event.from_user.id,
            username=event.from_user.username,
            language=event.from_user.language_code,
        )
        if not user.is_banned:
            data["user"] = user
            return await handler(event, data)
        return
