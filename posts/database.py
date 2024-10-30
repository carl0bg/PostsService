from .models import Posts
from photo.models import Photo
from .func_upload import get_path_upload_format
from video.models import Video
from document.models import Document

from django.db import transaction
from django.db.models import Count, Q


def bulk_create_media(post, media_files, model):
    if media_files:
        model.objects.bulk_create(
            [model(post=post, file=get_path_upload_format(post, media_file)) for media_file in media_files]
        )


def orm_delete_all(flag_delete: str, post):
    if flag_delete == 'all':
        post.photos.all().delete()
        post.videos.all().delete()
        post.documents.all().delete()
    elif flag_delete == 'photos':
        post.photos.all().delete()
    elif flag_delete == 'videos':
        post.videos.all().delete()
    elif flag_delete == 'documents':
        post.documents.all().delete()
    return post
        



@transaction.atomic
def create_post(validate_data, photos, videos, documents):
    post = Posts.objects.create(**validate_data)
    
    bulk_create_media(post, photos, Photo)
    bulk_create_media(post, videos, Video)
    bulk_create_media(post, documents, Document)
    
    return post




@transaction.atomic
def orm_put_post(post_id: int, validate_data: dict, photos, videos, documents):
    post = Posts.objects.select_related().get(id=post_id)
    post.user = validate_data.get('user', post.user)
    post.text = validate_data.get('text', post.text)
    post.chat = validate_data.get('chat', post.chat)

    orm_delete_all(flag_delete='all', post = post)

    bulk_create_media(post, photos, Photo)
    bulk_create_media(post, videos, Video)
    bulk_create_media(post, documents, Document)

    post.save()
    return post



@transaction.atomic
def orm_patch_post(post_id: int, validate_data: dict, photos, videos, documents):
    post = Posts.objects.get(id = post_id)
    post.user = validate_data['user']
    if validate_data['text'] is not None: 
        post.text = validate_data['text'] 
    else:
        post.text = None 


    if photos is not None: 
        orm_delete_all('photos', post)
        Photo.objects.bulk_create([Photo(post=post, file=get_path_upload_format(post, photo)) for photo in photos])    
    if videos is not None: 
        orm_delete_all('videos', post)
        Video.objects.bulk_create([Video(post=post, file=get_path_upload_format(post, video)) for video in videos])
    if documents is not None: 
        orm_delete_all('documents', post)
        Document.objects.bulk_create([Document(post=post, file=get_path_upload_format(post, document)) for document in documents])
    

    post.save()

    return post