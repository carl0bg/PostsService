from django.db import models
from django.utils.translation import gettext_lazy
from storages.backends.s3boto3 import S3Boto3Storage

<<<<<<< HEAD
from config.db_const import config
=======
from PostsService.settings import DOCUMENT_BUCKET_NAME, PHOTO_BUCKET_NAME, VIDEO_BUCKET_NAME


class DocumentStorage(S3Boto3Storage):
    bucket_name = DOCUMENT_BUCKET_NAME 

class VideoStorage(S3Boto3Storage):
    bucket_name = VIDEO_BUCKET_NAME 

class PhotoStorage(S3Boto3Storage):
    bucket_name = PHOTO_BUCKET_NAME 
>>>>>>> minio_v1


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
        null = True,
        blank=True,
    )

    document = models.FileField(
<<<<<<< HEAD
        storage=S3Boto3Storage(),
        null=True,
        blank = True,
    )

    photo = models.ImageField(
        storage=S3Boto3Storage(),
        null=True,
        blank = True,
    )
    
    video = models.FileField(
        storage=S3Boto3Storage(),
=======
        storage=DocumentStorage(),
        null=True,
        blank = True,
    )
    video = models.FileField(
        storage=VideoStorage(),
>>>>>>> minio_v1
        null=True,
        blank = True,
    )


    photo = models.ImageField(
        storage=PhotoStorage(),
        null=True,
        blank = True,
    )




    def __str__(self):
        return f'{self.id} - эл Posts'
    