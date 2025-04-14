import asyncio
import os
import time
from multiprocessing import Process, current_process

import django

# Устанавливаем переменную окружения для Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


def run_django():
    """Запуск Django сервера"""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен, "
            "находится в переменной окружения PYTHONPATH и виртуальное окружение активировано."
        ) from exc
    # Запуск Django сервера без автоматического перезапуска
    execute_from_command_line(["manage.py", "runserver", "--noreload"])


async def run_bot():
    """Асинхронный запуск Telegram-бота"""
    # Явно инициализируем Django перед любым использованием моделей
    import django

    django.setup()  # ВАЖНО: Это подготавливает Django для работы с ORM

    from tgbot.run import run_bot  # Импорт внутри функции после инициализации Django

    await run_bot()  # Запуск Telegram-бота


def start_bot():
    """Запуск бота Telegram в основном процессе"""
    asyncio.run(run_bot())


if __name__ == "__main__":
    if current_process().name == "MainProcess":
        # Сначала создаём процесс для запуска Django
        django_process = Process(target=run_django, name="DjangoProcess")

        # Запускаем процесс Django
        django_process.start()

        # Делаем паузу, чтобы сервер Django успел инициализироваться
        print("Ожидание инициализации сервера Django...")
        time.sleep(
            3
        )  # Настраиваемое время ожидания. Можно увеличить, если требуется больше времени.

        # Затем запускаем бота в основном процессе
        print("Запуск Telegram-бота...")
        start_bot()

        # Ждём завершения процесса Django (если потребуется)
        django_process.join()
