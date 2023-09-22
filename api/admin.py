from django.contrib import admin

# Register your models here.

from .models import chatRoom, message

admin.site.register(chatRoom)
admin.site.register(message)

