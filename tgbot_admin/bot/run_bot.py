from aiogram import Dispatcher, executor
from tgbot_admin.bot.app import middlewares, filters, handlers
from tgbot_admin.bot.loader import dp, bot
from tgbot_admin.bot.utils.logging import logger
from tgbot_admin.bot.app.middlewares import setup_middlewares

import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "django_core.settings"

django.setup()


async def on_startup(_):
    # from tgbot_admin.bot.app.commands import set_default_commands
    # await set_default_commands()
    logger.info("~ Bot_startup")


async def on_shutdown(dispatcher: Dispatcher):
    logger.info("~ Shutting down...")


async def runbot():
    setup_middlewares(dp)
    await on_startup(dp)
    await dp.start_polling()
    await on_shutdown(dp)
