from django.db import models
from django.utils.translation import gettext_lazy




class Posts(models.Model):

    class ChatType(models.TextChoices):
        PRIVATE = 'private'
        PUBLIC = 'public'

    created_date = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Время создание поста',
    )

    modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name = 'Время изменения поста',
    )

    chat = models.CharField(
        max_length=55,
        default=ChatType.PRIVATE,
        choices=ChatType.choices,
        verbose_name='Тип чата',
    )

    text = models.TextField(
        verbose_name='Текст поста',
        blank=True,
    )








    def __str__(self):
        return f'{self.id} - эл Posts'
    