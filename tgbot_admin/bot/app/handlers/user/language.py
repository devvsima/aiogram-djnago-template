from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from tgbot_admin.bot.loader import _, dp

from tgbot_admin.services import change_language

from tgbot_admin.bot.app.keyboards.inline.base import lang_ikb


@dp.message_handler(Command("language"))
@dp.message_handler(Command("lang"))
async def _lang(message: types.Message) -> None:
    """Предлагает клавиатуру с доступными языками"""
    await message.answer(
        _("Select the language you want to switch to: 🌐"),
        reply_markup=lang_ikb(),
    )


@dp.callback_query_handler(Text(["ru", "uk", "en"]))
async def _lang_change(callback: types.CallbackQuery) -> None:
    """Меняет язык пользователя на выбранный"""
    await change_language(callback.from_user.id, callback.data)
    await callback.message.edit_text(_("Your language has been successfully changed! ✅"))
