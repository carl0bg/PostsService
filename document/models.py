from django.db import models

from posts.storage import DocumentStorage, delete_type_from_s3

from posts.models import Posts
from django.dispatch import receiver
from posts.storage import VideoStorage, delete_type_from_s3
from django.db.models.signals import post_delete



class Document(models.Model):

    post = models.ForeignKey(
        to = Posts,
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



@receiver(post_delete, sender=Document)
def delete_all_type_from_s3(instance, **kwargs):
    bucket_name = DocumentStorage().bucket_name
    delete_type_from_s3(instance, bucket_name)