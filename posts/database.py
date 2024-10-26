from .models import Posts
from photo.models import Photo
from video.models import Video
from document.models import Document

from django.db import transaction
from django.db.models import Count, Q


def create_post(validate_data, photos, videos, documents):
    with transaction.atomic():
        post = Posts.objects.create(**validate_data)

        if photos is not None: Photo.objects.bulk_create([Photo(post=post, file=photo) for photo in photos])
        if videos is not None: Video.objects.bulk_create([Video(post=post, file=video) for video in videos])
        if documents is not None: Document.objects.bulk_create([Document(post=post, file=document) for document in documents])

    return post
