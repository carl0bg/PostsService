from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import User

# Register your models here.
@admin.register(User)
class PostsAdmin(ModelAdmin):
    list_display = ('id', 'username')
