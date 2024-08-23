import boto3

from django.db import models
from django.utils.translation import gettext_lazy
from django.db.models.signals import post_delete
from django.dispatch import receiver

from config.db_const import config
from .storage import PhotoStorage, DocumentStorage, VideoStorage
from .storage import delete_type_from_s3


class Photo(models.Model):
    post = models.ForeignKey(
        to = 'Posts',
        on_delete=models.CASCADE,
        related_name='photos'
    )
    
    file = models.ImageField(
        storage=PhotoStorage(),
        null=True,
        blank=True
    )

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_type_from_s3(self)

    def __str__(self):
        return f'Photo for post {self.post.id}'



class Video(models.Model):
    post = models.ForeignKey(
        to = 'Posts',
        on_delete=models.CASCADE,
        related_name='videos'
    )
    
    file = models.FileField(
        storage=VideoStorage(),
        null=True,
        blank=True
    )

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_type_from_s3(self)

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


    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_type_from_s3(self)


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


@receiver(post_delete, sender=Photo)
@receiver(post_delete, sender=Video)
@receiver(post_delete, sender=Document)
def delete_all_type_from_s3(instance, **kwargs):
    if isinstance(instance, Photo):
        bucket_name = PhotoStorage().bucket_name
    elif isinstance(instance, Video):
        bucket_name = VideoStorage().bucket_name
    elif isinstance(instance, Document):
        bucket_name = DocumentStorage().bucket_name
    delete_type_from_s3(instance, bucket_name)