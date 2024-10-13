from rest_framework import serializers

from photo.serializers import PhotoSerializers
from video.serializers import VideoSerializers
from document.serializers import DocumentSerializers
from photo.models import Photo
from video.models import Video
from document.models import Document


from .models import Posts



class PostSerializer(serializers.ModelSerializer):
    videos = VideoSerializers(many=False, required=False)
    photos = PhotoSerializers(many=False, required=False)
    documents = DocumentSerializers(many=False, required=False)

    class Meta:
        model = Posts
        fields = ('id', 'created_date', 'modified_date', 'chat', 'text', 'videos', 'photos', 'documents')
        read_only_fields = ('created_date', 'modified_date')

    def create(self, validated_data):
        videos_data = validated_data.pop('videos', None)
        photos_data = validated_data.pop('photos', None)
        documents_data = validated_data.pop('documents', None)
        
        post = Posts.objects.create(**validated_data)
        
        for video_data in videos_data:
            if videos_data[video_data] is not None:
                Video.objects.create(post=post, file = videos_data[video_data])
        for photo_data in photos_data:
            Photo.objects.create(post=post, file = photos_data[photo_data])
        for document_data in documents_data:
            Document.objects.create(post=post, file = documents_data[document_data])

        return post

    def update(self, instance, validated_data):
        videos_data = validated_data.pop('videos', [])
        photos_data = validated_data.pop('photos', [])
        documents_data = validated_data.pop('documents', [])
        
        instance.chat = validated_data.get('chat', instance.chat)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        
        # Update videos
        Video.objects.filter(post=instance).delete()
        for video_data in videos_data:
            Video.objects.create(post=instance, **video_data)

        # Update photos
        Photo.objects.filter(post=instance).delete()
        for photo_data in photos_data:
            Photo.objects.create(post=instance, **photo_data)

        # Update documents
        Document.objects.filter(post=instance).delete()
        for document_data in documents_data:
            Document.objects.create(post=instance, **document_data)

        return instance



# class PostSerializer(serializers.ModelSerializer):
#     videos = serializers.ListField(
#         child=serializers.FileField(),
#         required=False
#     )
#     photos = serializers.ListField(
#         child=serializers.ImageField(),
#         required=False
#     )
#     documents = serializers.ListField(
#         child=serializers.FileField(),
#         required=False
#     )

#     class Meta:
#         model = Posts
#         fields = ('id', 'created_date', 'modified_date', 'chat', 'text', 'videos', 'photos', 'documents')
#         read_only_fields = ('created_date', 'modified_date')

#     def create(self, validated_data):
#         videos_data = validated_data.pop('videos', [])
#         photos_data = validated_data.pop('photos', [])
#         documents_data = validated_data.pop('documents', [])
        
#         post = Posts.objects.create(**validated_data)
        
#         for video_file in videos_data:
#             Video.objects.create(post=post, file=video_file)
#         for photo_file in photos_data:
#             Photo.objects.create(post=post, file=photo_file)
#         for document_file in documents_data:
#             Document.objects.create(post=post, file=document_file)

#         return post

#     def update(self, instance, validated_data):
#         videos_data = validated_data.pop('videos', [])
#         photos_data = validated_data.pop('photos', [])
#         documents_data = validated_data.pop('documents', [])
        
#         instance.chat = validated_data.get('chat', instance.chat)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
        
#         # Обновляем видео
#         Video.objects.filter(post=instance).delete()
#         for video_file in videos_data:
#             Video.objects.create(post=instance, file=video_file)

#         # Обновляем фото
#         Photo.objects.filter(post=instance).delete()
#         for photo_file in photos_data:
#             Photo.objects.create(post=instance, file=photo_file)

#         # Обновляем документы
#         Document.objects.filter(post=instance).delete()
#         for document_file in documents_data:
#             Document.objects.create(post=instance, file=document_file)

#         return instance


# class PostSerializer(serializers.ModelSerializer):
#     videos = serializers.ListField(
#         child=serializers.FileField(),
#         required=False
#     )
#     photos = serializers.ListField(
#         child=serializers.ImageField(),
#         required=False
#     )
#     documents = serializers.ListField(
#         child=serializers.FileField(),
#         required=False
#     )

#     class Meta:
#         model = Posts
#         fields = ('id', 'created_date', 'modified_date', 'chat', 'text', 'videos', 'photos', 'documents')
#         read_only_fields = ('created_date', 'modified_date')

#     def create(self, validated_data):
#         videos_data = validated_data.pop('videos', [])
#         photos_data = validated_data.pop('photos', [])
#         documents_data = validated_data.pop('documents', [])
        
#         post = Posts.objects.create(**validated_data)
        
#         for video_file in videos_data:
#             Video.objects.create(post=post, file=video_file)
#         for photo_file in photos_data:
#             Photo.objects.create(post=post, file=photo_file)
#         for document_file in documents_data:
#             Document.objects.create(post=post, file=document_file)

#         return post

#     def update(self, instance, validated_data):
#         videos_data = validated_data.pop('videos', [])
#         photos_data = validated_data.pop('photos', [])
#         documents_data = validated_data.pop('documents', [])
        
#         instance.chat = validated_data.get('chat', instance.chat)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
        
#         # Update videos
#         Video.objects.filter(post=instance).delete()
#         for video_file in videos_data:
#             Video.objects.create(post=instance, file=video_file)

#         # Update photos
#         Photo.objects.filter(post=instance).delete()
#         for photo_file in photos_data:
#             Photo.objects.create(post=instance, file=photo_file)

#         # Update documents
#         Document.objects.filter(post=instance).delete()
#         for document_file in documents_data:
#             Document.objects.create(post=instance, file=document_file)

#         return instance
