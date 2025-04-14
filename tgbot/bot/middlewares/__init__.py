from aiogram import Dispatcher

from tgbot.bot.middlewares.i18n import i18n_middleware
from tgbot.bot.routers import admin_router, start_router, user_router

from .admin import AdminMiddleware
from .start import StartMiddleware
from .user import UsersMiddleware


def setup_middlewares(dp: Dispatcher) -> None:
    start_router.message.middleware(StartMiddleware())
    start_router.message.middleware(i18n_middleware)

    admin_router.message.middleware(AdminMiddleware())
    admin_router.message.middleware(i18n_middleware)

    user_router.message.middleware(UsersMiddleware())
    user_router.callback_query.middleware(UsersMiddleware())
    user_router.message.middleware(i18n_middleware)
