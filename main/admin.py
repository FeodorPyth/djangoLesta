from django.contrib import admin

from .models import Word


@admin.register(Word)
class CommonAdmin(admin.ModelAdmin):
    pass
