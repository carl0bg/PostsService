from django.db import models
from django.utils.translation import gettext_lazy
from storages.backends.s3boto3 import S3Boto3Storage



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

    document = models.FileField(
        storage=S3Boto3Storage(location = 'document'),
        null=True,
        blank = True,
    )
    video = models.FileField(
        storage=S3Boto3Storage(location = 'video'),
        null=True,
        blank = True,
    )


    photo = models.ImageField(
        storage=S3Boto3Storage(location = 'photo'),
        null=True,
        blank = True,
    )






    def __str__(self):
        return f'{self.id} - эл Posts'
    