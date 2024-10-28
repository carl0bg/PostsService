from rest_framework import serializers

from .models import Posts
from .database import create_post, orm_put_post, orm_patch_post

from video.serializers import VideoSerializers
from document.serializers import DocumentSerializers
from photo.serializers import PhotoSerializers


class PostSerializer(serializers.ModelSerializer):
    documents = DocumentSerializers(many = True, required=False)
    photos = PhotoSerializers(many = True, required=False)
    videos = VideoSerializers(many = True, required=False)

    class Meta:
        model = Posts
        fields = ['id', 'documents', 'photos', 'videos', 'chat', 'text', 'user']
        
    def create(self, validated_data):
        photos_data = validated_data.pop('photos', None)
        documents_data = validated_data.pop('documents', None)
        videos_data = validated_data.pop('videos', None)        
        post = create_post(validated_data, photos_data, videos_data, documents_data)

        return post
    

    def update(self, post: Posts, validated_data: dict) -> Posts:
        photos_data = validated_data.pop('photos', None)
        documents_data = validated_data.pop('documents', None)
        videos_data = validated_data.pop('videos', None)

        if validated_data['method'] == "PUT":
            del validated_data['method'] 
            post = orm_put_post(post.id, validated_data, photos_data, videos_data, documents_data)
            return post
        else: #PATCH
            del validated_data['method'] 
            post = orm_patch_post(post.id, validated_data, photos_data, videos_data, documents_data)
            return post
