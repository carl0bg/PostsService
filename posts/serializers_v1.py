# from rest_framework import serializers

# from photo.serializers import PhotoSerializers
# from video.serializers import VideoSerializers
# from document.serializers import DocumentSerializers
# from photo.models import Photo
# from video.models import Video
# from document.models import Document


# from .models import Posts



# class PostSerializer(serializers.ModelSerializer):
#     videos = VideoSerializers(many=True, required=False)
#     photos = PhotoSerializers(many=True, required=False)
#     documents = DocumentSerializers(many=True, required=False)

#     class Meta:
#         model = Posts
#         fields = ('id', 'created_date', 'modified_date', 'chat', 'text', 'videos', 'photos', 'documents')
#         read_only_fields = ('created_date', 'modified_date')

#     def create(self, validated_data):
#         videos_data = validated_data.pop('videos', None)
#         photos_data = validated_data.pop('photos', None)
#         documents_data = validated_data.pop('documents', None)
        
#         post = Posts.objects.create(**validated_data)
        
#         for video_data in videos_data:
#             if videos_data[video_data] is not None:
#                 Video.objects.create(post=post, file = videos_data[video_data])
#         for photo_data in photos_data:
#             if photos_data[photo_data] is not None:
#                 Photo.objects.create(post=post, file = photos_data[photo_data])
#         for document_data in documents_data:
#             if documents_data[document_data] is not None:
#                 Document.objects.create(post=post, file = documents_data[document_data])

#         return post




#     def update(self, instance, validated_data):
#             videos_data = validated_data.pop('videos', None)
#             if videos_data is None or videos_data['file'] is None:
#                 videos_data = None

#             photos_data = validated_data.pop('photos', None)
#             if photos_data is None or photos_data['file'] is None:
#                 photos_data = None

#             documents_data = validated_data.pop('documents', None)
#             if documents_data is None or documents_data['file'] is None:
#                 documents_data = None
            
#             instance.chat = validated_data.get('chat', instance.chat)
#             instance.text = validated_data.get('text', instance.text)
#             instance.save()

#             # Если используется PUT и данные отсутствуют, удалить существующие записи
#             request_method = self.context['request'].method
#             if request_method == 'PUT':
#                 if videos_data is None:
#                     Video.objects.filter(post=instance).delete()
#                 if photos_data is None:
#                     Photo.objects.filter(post=instance).delete()
#                 if documents_data is None:
#                     Document.objects.filter(post=instance).delete()

#             # Обновление видео
#             if videos_data is not None:
#                 existing_video_ids = {video_data.get('id') for video_data in videos_data if video_data.get('id')}
#                 Video.objects.filter(post=instance).exclude(id__in=existing_video_ids).delete()
#                 for video_data in videos_data:
#                     video_id = video_data.get('id', None)
#                     if video_id:
#                         video_instance = Video.objects.filter(id=video_id, post=instance).first()
#                         if video_instance:
#                             for attr, value in video_data.items():
#                                 setattr(video_instance, attr, value)
#                             video_instance.save()
#                         else:
#                             Video.objects.create(post=instance, **video_data)
#                     else:
#                         Video.objects.create(post=instance, **video_data)

#             # Обновление фото
#             if photos_data is not None:
#                 existing_photo_ids = {photo_data.get('id') for photo_data in photos_data if photo_data.get('id')}
#                 Photo.objects.filter(post=instance).exclude(id__in=existing_photo_ids).delete()
#                 for photo_data in photos_data:
#                     photo_id = photo_data.get('id', None)
#                     if photo_id:
#                         photo_instance = Photo.objects.filter(id=photo_id, post=instance).first()
#                         if photo_instance:
#                             for attr, value in photo_data.items():
#                                 setattr(photo_instance, attr, value)
#                             photo_instance.save()
#                         else:
#                             Photo.objects.create(post=instance, **photo_data)
#                     else:
#                         Photo.objects.create(post=instance, **photo_data)

#             # Обновление документов
#             if documents_data is not None:
#                 existing_document_ids = {document_data.get('id') for document_data in documents_data if document_data.get('id')}
#                 Document.objects.filter(post=instance).exclude(id__in=existing_document_ids).delete()
#                 for document_data in documents_data:
#                     document_id = document_data.get('id', None)
#                     if document_id:
#                         document_instance = Document.objects.filter(id=document_id, post=instance).first()
#                         if document_instance:
#                             for attr, value in document_data.items():
#                                 setattr(document_instance, attr, value)
#                             document_instance.save()
#                         else:
#                             Document.objects.create(post=instance, **document_data)
#                     else:
#                         Document.objects.create(post=instance, **document_data)

#             return instance




    # def update(self, instance, validated_data):
    #     videos_data = validated_data.pop('videos', None)
    #     photos_data = validated_data.pop('photos', None)
    #     documents_data = validated_data.pop('documents', None)
        
    #     instance.chat = validated_data.get('chat', instance.chat)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.save()

    #     # Update videos
    #     if videos_data is not None:
    #         for video_data in videos_data:
    #             video_id = video_data.get('id', None)
    #             if video_id:
    #                 video_instance = Video.objects.filter(id=video_id, post=instance).first()
    #                 if video_instance:
    #                     # Update existing video
    #                     for attr, value in video_data.items():
    #                         setattr(video_instance, attr, value)
    #                     video_instance.save()
    #                 else:
    #                     # Create new video if not found
    #                     Video.objects.create(post=instance, **video_data)
    #             else:
    #                 # Create new video if no ID provided
    #                 Video.objects.create(post=instance, **video_data)

    #     # Update photos
    #     if photos_data is not None:
    #         for photo_data in photos_data:
    #             photo_id = photo_data.get('id', None)
    #             if photo_id:
    #                 photo_instance = Photo.objects.filter(id=photo_id, post=instance).first()
    #                 if photo_instance:
    #                     # Update existing photo
    #                     for attr, value in photo_data.items():
    #                         setattr(photo_instance, attr, value)
    #                     photo_instance.save()
    #                 else:
    #                     # Create new photo if not found
    #                     Photo.objects.create(post=instance, **photo_data)
    #             else:
    #                 # Create new photo if no ID provided
    #                 Photo.objects.create(post=instance, **photo_data)

    #     # Update documents
    #     if documents_data is not None:
    #         for document_data in documents_data:
    #             document_id = document_data.get('id', None)
    #             if document_id:
    #                 document_instance = Document.objects.filter(id=document_id, post=instance).first()
    #                 if document_instance:
    #                     # Update existing document
    #                     for attr, value in document_data.items():
    #                         setattr(document_instance, attr, value)
    #                     document_instance.save()
    #                 else:
    #                     # Create new document if not found
    #                     Document.objects.create(post=instance, **document_data)
    #             else:
    #                 # Create new document if no ID provided
    #                 Document.objects.create(post=instance, **document_data)

    #     return instance

    # def update(self, instance, validated_data):
    #     videos_data = validated_data.pop('videos', [])
    #     photos_data = validated_data.pop('photos', [])
    #     documents_data = validated_data.pop('documents', [])
        
    #     instance.chat = validated_data.get('chat', instance.chat)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.save()
        
    #     # Update videos
    #     Video.objects.filter(post=instance).delete()
    #     for video_data in videos_data:
    #         Video.objects.create(post=instance, **video_data)

    #     # Update photos
    #     Photo.objects.filter(post=instance).delete()
    #     for photo_data in photos_data:
    #         Photo.objects.create(post=instance, **photo_data)

    #     # Update documents
    #     Document.objects.filter(post=instance).delete()
    #     for document_data in documents_data:
    #         Document.objects.create(post=instance, **document_data)

    #     return instance



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
