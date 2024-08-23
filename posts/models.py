from django.db import models
from django.utils.translation import gettext_lazy
from storages.backends.s3boto3 import S3Boto3Storage

from PostsService.settings import DOCUMENT_BUCKET_NAME, PHOTO_BUCKET_NAME, VIDEO_BUCKET_NAME
from storages.backends.s3boto3 import S3Boto3Storage
import boto3
from config.db_const import config


class DocumentStorage(S3Boto3Storage):
    bucket_name = DOCUMENT_BUCKET_NAME 

class VideoStorage(S3Boto3Storage):
    bucket_name = VIDEO_BUCKET_NAME 

class PhotoStorage(S3Boto3Storage):
    bucket_name = PHOTO_BUCKET_NAME 



class Photo(models.Model):
    post = models.ForeignKey(
        to = 'Posts',
        on_delete=models.CASCADE,
        related_name='photos'
    )
    
    image = models.ImageField(
        storage=PhotoStorage(),
        null=True,
        blank=True
    )


    def delete_photo_from_s3(self):
        s3_client = boto3.client(
            's3',
            aws_access_key_id=config.aws_access_key_id,
            aws_secret_access_key=config.aws_secret_access_key,
            endpoint_url=config.aws_s3_endpoint_url
        )
        bucket_name = PHOTO_BUCKET_NAME
        key = self.image.name
        print(key)
        print(bucket_name)

        try:
            s3_client.delete_object(Bucket=bucket_name, Key=key)
        except Exception as e:
            print(e)


    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.delete_photo_from_s3()


    def __str__(self):
        return f'Photo for post {self.post.id}'


class Video(models.Model):
    post = models.ForeignKey(
        to = 'Posts',
        on_delete=models.CASCADE,
        related_name='videos'
    )
    
    video_file = models.FileField(
        storage=VideoStorage(),
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Video for post {self.post.id}'


class Document(models.Model):

    post = models.ForeignKey(
        to = 'Posts',
        on_delete=models.CASCADE,
        related_name='documents'
    )
    
    file = models.FileField(
        storage=DocumentStorage(),
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Document for post {self.post.id}'



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

    def __str__(self):
        return f'Post {self.id}'
