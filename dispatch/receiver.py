from django.dispatch import receiver
from django.db.models.signals import post_delete

from photo.models import Photo
from document.models import Document
from video.models import Video
from posts.storage import PhotoStorage, DocumentStorage, VideoStorage, delete_type_from_s3




@receiver(post_delete, sender=Photo)
@receiver(post_delete, sender=Video)
@receiver(post_delete, sender=Document)
def delete_all_type_from_s3(instance, **kwargs):
    print('hellllo')
    if isinstance(instance, Photo):
        bucket_name = PhotoStorage().bucket_name
    elif isinstance(instance, Video):
        bucket_name = VideoStorage().bucket_name
    elif isinstance(instance, Document):
        bucket_name = DocumentStorage().bucket_name
    delete_type_from_s3(instance, bucket_name)