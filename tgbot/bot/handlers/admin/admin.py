from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from tgbot.bot.routers import admin_router as router

from tgbot.bot.handlers.msg_text import msg_text


@router.message(Command("admin"), StateFilter(None))
async def _admin_command(message: types.Message) -> None:
    """Админ панель"""
    await message.answer(msg_text.ADMIN_WELCOME)
