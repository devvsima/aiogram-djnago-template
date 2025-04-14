from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n

from app.settings import redis, tgbot
from tgbot.utils.logging import logger

if redis.URL:
    from aiogram.fsm.storage.redis import RedisStorage
    from redis.asyncio.client import Redis

    storage = RedisStorage(Redis.from_url(redis.URL))
    logger.info("Storage: Redis")
elif not redis.URL:
    from aiogram.fsm.storage.memory import MemoryStorage

    storage = MemoryStorage()
    logger.info("Storage: Default")

bot = Bot(
    tgbot.TG_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher(bot=bot, storage=storage)

i18n = I18n(path=tgbot.LOCALES_DIR, domain=tgbot.I18N_DOMAIN)
_ = i18n.gettext
