from django.contrib import admin
from .models import *


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'slug', 'image', 'soundfile', 'cat']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
