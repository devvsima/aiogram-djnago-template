from pathlib import Path

from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-t+!bmwe=6gk11!97s75v@@txwfs2iq1(7_1oep4rn4u*32l%6*"

DEBUG = env.bool("server_debug", default=True)

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    env.str("server_ip", default=None),
    env.str("server_domain", default=None),
]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tgbot",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [f"{BASE_DIR}/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# ---< Telegram bot >---
class TelegramBotSettings:
    TG_TOKEN: str = env.str("TOKEN", default=None)
    ADMINS: list = env.list("ADMINS", default=None, subcast=int)
    SKIP_UPDATES: bool = env.bool("SKIP_UPDATES", default=False)

    I18N_DOMAIN = "bot"

    LOCALES_DIR = f"{BASE_DIR}/tgbot/locales"
    LOGS_DIR = f"{BASE_DIR}/tgbot/logs/logs.log"


tg_settings = TelegramBotSettings()

# ---< Database >---

DB_NAME: str = env.str("DB_NAME", default=None)
DB_HOST: str = env.str("DB_HOST", default="localhost")
DB_PORT: int = env.int("DB_PORT", default=5432)
DB_USER: str = env.str("DB_USER", default="postgres")
DB_PASS: str = env.str("DB_PASS", default="postgres")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASS,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
    if all([DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASS])
    else {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "database.sqlite3",
    }
}


# ---< Redis >---
REDIS_HOST: str = env.str("REDIS_HOST", default=None)
REDIS_PORT: int = env.int("REDIS_PORT", default=6379)
REDIS_DB: int = env.int("REDIS_DB", default=5)

REDIS_URL: str = env.str("RD_URI", default=None)

if all([REDIS_DB, REDIS_HOST, REDIS_PORT]):
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"


# ---< Other >---
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"


MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "media/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/user/login/"
