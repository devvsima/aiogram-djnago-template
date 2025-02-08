from tgbot_admin.bot.loader import dp
from .admin import IsAdmin

if __name__ == "bot.filters":
    dp.filters_factory.bind(IsAdmin)
