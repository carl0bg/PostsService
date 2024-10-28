from .models import Posts
from photo.models import Photo
from .func_upload import get_path_upload_format
from video.models import Video
from document.models import Document

from django.db import transaction
from django.db.models import Count, Q




@transaction.atomic
def create_post(validate_data, photos, videos, documents):
    post = Posts.objects.create(**validate_data)

    if photos is not None: Photo.objects.bulk_create([Photo(post=post, file=get_path_upload_format(post, photo)) for photo in photos])    
    if videos is not None: Video.objects.bulk_create([Video(post=post, file=get_path_upload_format(post, video)) for video in videos])
    if documents is not None: Document.objects.bulk_create([Document(post=post, file=get_path_upload_format(post, document)) for document in documents])

    return post



@transaction.atomic
def orm_put_post(post_id: int, validate_data: dict, photos, videos, documents):
    post = Posts.objects.get(id = post_id)
    post.photos.all().delete() 
    post.documents.all().delete() 
    post.videos.all().delete()

    if validate_data['text'] is not None: post.text = validate_data['text']
    if validate_data['chat'] is not None: post.chat = validate_data['chat']

    if photos is not None: Photo.objects.bulk_create([Photo(post=post, file=get_path_upload_format(post, photo)) for photo in photos])    
    if videos is not None: Video.objects.bulk_create([Video(post=post, file=get_path_upload_format(post, video)) for video in videos])
    if documents is not None: Document.objects.bulk_create([Document(post=post, file=get_path_upload_format(post, document)) for document in documents])

    post.save()

    return post


@transaction.atomic
def orm_patch_post(post_id: int, validate_data: dict, photos, videos, documents):
    post = Posts.objects.get(id = post_id)
    if validate_data['text'] is not None: 
        post.text = validate_data['text'] 
    else:
        post.text = None 


    if photos is not None: 
        post.photos.all().delete()
        Photo.objects.bulk_create([Photo(post=post, file=get_path_upload_format(post, photo)) for photo in photos])    
    if videos is not None: 
        post.videos.all().delete()
        Video.objects.bulk_create([Video(post=post, file=get_path_upload_format(post, video)) for video in videos])
    if documents is not None: 
        post.documents.all().delete() 
        Document.objects.bulk_create([Document(post=post, file=get_path_upload_format(post, document)) for document in documents])
    

    post.save()

    return post