from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import TestUser

# Register your models here.
@admin.register(TestUser)
class PostsAdmin(ModelAdmin):
    list_display = ('id', 'username')
