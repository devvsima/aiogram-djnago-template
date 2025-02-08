from logging import getLogger
from app.settings import tg_settings
from loguru import logger

logger.add(
    tg_settings.LOGS_DIR,
    format="[{time}] [{level}] [{file.name}:{line}]  {message}",
    level="DEBUG",
    rotation="1 month",
    compression="zip",
)

getLogger("aiogram").addFilter(
    lambda r: r.getMessage().find("Field 'database_user' doesn't exist in") == -1
)
