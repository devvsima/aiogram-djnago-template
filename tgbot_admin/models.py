from django.db import models
from datetime import datetime


class TgUsers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    language = models.CharField(max_length=50)  # Добавь max_length
    username = models.CharField(max_length=150, null=True, blank=True)  # Добавь max_length
    referral = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


# from django.db import models
# from django.utils import timezone
# from asgiref.sync import sync_to_async
# from django.db import close_old_connections
# from django.db import models


# class Event(models.Model):
#     title = models.CharField(max_length=255)  # Название события
#     description = models.TextField()  # Описание события
#     data = models.JSONField()  # Поле для хранения данных в формате JSON

#     class Meta:
#         verbose_name = "Событие"
#         verbose_name_plural = "События"

#     def __str__(self):
#         return self.title


# # Create your models here.
# class TodoList(models.Model):
#     title = models.CharField(max_length=250)
#     content = models.TextField(blank=True)  # Текстовое поле
#     created = models.DateField(default=timezone.now)  # Дата создания

#     class Meta:
#         ordering = ["-created"]  # Сортировка дел по времени их создания

#     def __str__(self):
#         return self.title


# @sync_to_async
# def get_list():
#     return TodoList.objects.all()


# # async def get_list():
# #     @sync_to_async
# #     def _get_user():
# #         close_old_connections()
# #         return TodoList.objects.all()
# #     return await _get_user()
