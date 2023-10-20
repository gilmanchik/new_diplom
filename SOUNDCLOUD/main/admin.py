from django.contrib import admin
from .models import *


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'slug', 'image', 'soundfile', 'release', 'cat']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['release']


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
