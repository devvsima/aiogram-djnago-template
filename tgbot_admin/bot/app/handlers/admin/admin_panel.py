from aiogram import types
from aiogram.dispatcher.filters import Command

from tgbot_admin.bot.app.filters.admin import IsAdmin
from tgbot_admin.bot.loader import _, dp


@dp.message_handler(IsAdmin(), Command("admin"))
async def _admin_command(message: types.Message):
    await message.answer(_("You admin!"))
