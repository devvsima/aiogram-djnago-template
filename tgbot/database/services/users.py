from ..models.tgusers import TgUsers
from django.db.utils import IntegrityError

from ...utils.logging import logger


async def get_user(user_id: int) -> TgUsers | None:
    """
    Возвращает пользователя по его ID (или None, если пользователь не найден).
    """
    return await TgUsers.objects.filter(id=user_id).afirst()


async def create_user(user_id: int, username: str = None, language: str = None) -> TgUsers:
    """
    Создает нового пользователя.
    """
    logger.info(f"New user: {user_id} | {username}")
    try:
        return await TgUsers.objects.acreate(id=user_id, username=username, language=language)
    except IntegrityError:
        # Если пользователь уже существует из-за гонки данных, возвращаем его
        return await get_user(user_id)


async def get_or_create_user(user_id: int, username: str = None, language: str = None) -> TgUsers:
    """
    Возвращает пользователя по его ID.
    Если пользователь отсутствует, создает его.
    """
    user = await get_user(user_id)
    if user:
        return user
    return await create_user(user_id, username, language)


async def update_user_username(user_id: int, username: str = None) -> None:
    """
    Обновляет username (имя пользователя) для указанного ID.
    """
    await TgUsers.objects.filter(id=user_id).aupdate(username=username)
    logger.info(f"Update user: {user_id} | {username}")


async def change_language(user_id: int, language: str) -> None:
    """
    Изменяет язык пользователя.
    """
    await TgUsers.objects.filter(id=user_id).aupdate(language=language)
    logger.info(f"User: {user_id} | изменил язык на - {language}")


async def ban_or_unban_user(user_id: int, is_banned: bool) -> None:
    """
    Блокирует или разблокирует пользователя.
    """
    await TgUsers.objects.filter(id=user_id).aupdate(is_banned=is_banned)
    logger.info(f"User: {user_id} | стату блокироваки изминен на - {is_banned}")


async def new_referral(inviter_id: int) -> None:
    """
    Увеличивает счетчик рефералов для пользователя.
    """
    user = await TgUsers.objects.filter(id=inviter_id).afirst()

    if user:
        await TgUsers.objects.filter(id=inviter_id).aupdate(referral=user.referral + 1)
    logger.info(f"User: {inviter_id} | привел нового пользователя")
