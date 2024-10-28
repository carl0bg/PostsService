from django.db import models

from posts.storage import PhotoStorage, delete_type_from_s3
from posts.models import Posts
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_delete

from posts.func_upload import get_path_upload_format




class Photo(models.Model):
    post = models.ForeignKey(
        to = Posts,
        on_delete=models.CASCADE,
        related_name='photos',
        null = True, #TODO
        blank= True
    )
    
    file = models.ImageField(
        storage=PhotoStorage(),
        null=True,
        blank=True
    )



    def save(self, *args, **kwargs):
        self.file.name = get_path_upload_format(
            post = self.post,
            file = self.file.name
        )
        super().save(*args, **kwargs)



    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_type_from_s3(self)

    def __str__(self):
        return f'Photo for post {self.post.id}'
    
    class Meta:
        db_table = 'photo'



@receiver(post_delete, sender=Photo)
def delete_all_type_from_s3(instance, **kwargs):
    bucket_name = PhotoStorage().bucket_name
    delete_type_from_s3(instance, bucket_name)
