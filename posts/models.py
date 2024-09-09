import boto3

from django.db import models


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


    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f'Post {self.id}'


