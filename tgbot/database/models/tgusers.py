from django.db import models


class TgUsers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    language = models.CharField(max_length=50)
    username = models.CharField(max_length=150, null=True, blank=True)
    referral = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tgusers"
        verbose_name = "TgUser"
        verbose_name_plural = "TgUsers"

    def __str__(self) -> str:
        return f"{self.id} | {self.username}"
