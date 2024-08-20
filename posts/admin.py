from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Posts


@admin.register(Posts)
class PostsAdmin(ModelAdmin):
    list_display = ('id', 'chat', 'created_date', 'modified_date')
