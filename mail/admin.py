from django.contrib import admin
from .models import MailMessage,Task


admin.site.register(MailMessage)
admin.site.register(Task)
