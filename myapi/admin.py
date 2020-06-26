from django.contrib import admin
from .models import Hero


class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias')
    list_display_links = ('name',)


admin.site.register(Hero)
