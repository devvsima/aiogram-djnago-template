from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from tgbot.loader import bot

from tgbot.database.models.tgusers import TgUsers

from tgbot.bot.routers import user_router as router
from tgbot.bot.handlers.msg_text import msg_text

from tgbot.utils.base62 import encode_base62


@router.message(Command("invite"), StateFilter(None))
async def _invite_link_command(message: types.Message, user: TgUsers) -> None:
    """Дает пользователю его реферальную ссылку"""
    bot_user = await bot.get_me()
    user_code: str = encode_base62(message.from_user.id)

    await message.answer(
        msg_text.INVITE_FRIENDS.format(
            user.referral,
            bot_user.username,
            user_code,
        )
    )
