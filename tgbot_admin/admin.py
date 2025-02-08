from django.contrib import admin

# Register your models here.
from .models import TgUsers


admin.site.register([TgUsers])
