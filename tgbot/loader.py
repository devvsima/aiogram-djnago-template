from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n

from app.settings import tg_settings, REDIS_URL
from tgbot.utils.logging import logger

if REDIS_URL:
    from aiogram.fsm.storage.redis import RedisStorage
    from redis.asyncio.client import Redis

    storage = RedisStorage(Redis.from_url(REDIS_URL))
    logger.info("Storage: Redis")
elif not REDIS_URL:
    from aiogram.fsm.storage.memory import MemoryStorage

    storage = MemoryStorage()
    logger.info("Storage: Default")

bot = Bot(
    tg_settings.TG_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher(bot=bot, storage=storage)

i18n = I18n(path=tg_settings.LOCALES_DIR, domain=tg_settings.I18N_DOMAIN)
_ = i18n.gettext
