import boto3

from django.db import models
from TestUser.models import User

class Posts(models.Model):

    class ChatType(models.TextChoices):
        PRIVATE = 'private'
        PUBLIC = 'public'

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создание поста'
    )

    modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Время изменения поста'
    )

    chat = models.CharField(
        max_length=55,
        default=ChatType.PRIVATE,
        choices=ChatType.choices, 
        verbose_name='Тип чата'
    )
    
    text = models.TextField(
        verbose_name='Текст поста',
        blank=True
    )
    
    user = models.ForeignKey(
        to = User,
        on_delete=models.CASCADE,
        related_name = 'post_user',
        # blank=True,
        # null=False,
    )

    class Meta:
        db_table = 'posts'




