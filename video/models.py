from django.db import models

from posts.storage import VideoStorage, delete_type_from_s3
from posts.models import Posts

from django.dispatch import receiver
from django.db.models.signals import post_delete
from posts.storage import VideoStorage, delete_type_from_s3


class Video(models.Model):
    post = models.ForeignKey(
        to = Posts,
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
    
    class Meta:
        db_table = 'video'


@receiver(post_delete, sender=Video)
def delete_all_type_from_s3(instance, **kwargs):
    bucket_name = VideoStorage().bucket_name
    delete_type_from_s3(instance, bucket_name)