from pathlib import Path
from environs import Env

DIR = Path(__file__).absolute().parent.parent

env = Env()
env.read_env()

# ---< Telegram bot >---
TG_TOKEN: str = env.str("TOKEN", default=None)
ADMINS: list = env.list("ADMINS", default=None, subcast=int)
SKIP_UPDATES: bool = env.bool("SKIP_UPDATES", default=False)

# ---< Redis >---
REDIS_HOST: str = env.str("REDIS_HOST", default=None)
REDIS_PORT: int = env.int("REDIS_PORT", default=6379)
REDIS_DB: int = env.int("REDIS_DB", default=5)

REDIS_URL: str = env.str("RD_URI", default=None)

# ---< Other >---
I18N_DOMAIN = "bot"

IMAGES_DIR = rf"{DIR}/images"
LOCALES_DIR = f"{DIR}/data/locales"
