from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ConctactAdmin(admin.ModelAdmin):
    ...