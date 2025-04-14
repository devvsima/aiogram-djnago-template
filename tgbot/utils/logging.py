from logging import getLogger

from loguru import logger

from app.settings import tgbot

logger.add(
    tgbot.LOGS_DIR,
    format="[{time}] [{level}] [{file.name}:{line}]  {message}",
    level="DEBUG",
    rotation="1 month",
    compression="zip",
)

getLogger("aiogram").addFilter(
    lambda r: r.getMessage().find("Field 'database_user' doesn't exist in") == -1
)
