from aiogram import types
from aiogram.dispatcher.filters import Command, CommandHelp

from tgbot_admin.bot.loader import _, dp


@dp.message_handler(Command("Help 🆘"))
@dp.message_handler(CommandHelp())
async def _help_command(message: types.Message):
    await message.answer(_("Help 🆘"))
