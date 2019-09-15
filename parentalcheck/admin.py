from django.contrib import admin

from .models import DangerType, Danger, Content

# Register your models here.
admin.site.register(DangerType)
admin.site.register(Danger)
admin.site.register(Content)