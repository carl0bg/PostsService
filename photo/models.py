from django.db import models

from posts.storage import PhotoStorage, delete_type_from_s3
from posts.models import Posts
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Photo(models.Model):
    post = models.ForeignKey(
        to = Posts,
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



@receiver(post_delete, sender=Photo)
def delete_all_type_from_s3(instance, **kwargs):
    print('helllllllllllllllllllllllllllllllllllllllllllllllllllleeee')
    bucket_name = PhotoStorage().bucket_name
    delete_type_from_s3(instance, bucket_name)
