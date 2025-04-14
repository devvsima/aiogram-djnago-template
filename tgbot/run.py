import asyncio
from aiogram.methods import DeleteWebhook

from tgbot.loader import dp, bot
from app.settings import tgbot
from tgbot.utils.logging import logger

from tgbot.bot.handlers import setup_handlers
from tgbot.bot.middlewares import setup_middlewares


async def on_startup() -> None:
    from tgbot.bot.others.commands import set_default_commands

    await set_default_commands()
    logger.info("~ Bot startup")


async def on_shutdown() -> None:
    logger.info("~ Bot shutting down...")


async def run_bot():
    setup_middlewares(dp)
    setup_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await bot(DeleteWebhook(drop_pending_updates=tgbot.SKIP_UPDATES))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_bot())
