from .models import Posts
from photo.models import Photo
from .func_upload import get_path_upload_format
from video.models import Video
from document.models import Document

from django.db import transaction
from django.db.models import Count, Q


def create_post(validate_data, photos, videos, documents):
    with transaction.atomic():
        post = Posts.objects.create(**validate_data)

        if photos is not None: Photo.objects.bulk_create([Photo(post=post, file=get_path_upload_format(post, photo)) for photo in photos])    
        if videos is not None: Video.objects.bulk_create([Video(post=post, file=get_path_upload_format(post, video)) for video in videos])
        if documents is not None: Document.objects.bulk_create([Document(post=post, file=get_path_upload_format(post, document)) for document in documents])

    return post
