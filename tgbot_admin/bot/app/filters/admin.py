from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from tgbot_admin.bot.data.config import ADMINS


class IsAdmin(BoundFilter):
    async def check(self, message: Message):
        return bool(int(message.from_user.id) in ADMINS)
