from rest_framework import serializers

from .models import Posts

from video.models import Video
from photo.models import Photo
from document.models import Document


class VideoSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'file', 'post')


class DocumentSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'file', 'post')



class PhotoSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'file', 'post')

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)



class PostSerializer(serializers.ModelSerializer):
    documents = DocumentSerializers2(many = True, required=False)
    photos = PhotoSerializers2(many = False, required=False)
    videos = VideoSerializers2(many = True, required=False)


    class Meta:
        model = Posts
        fields = '__all__'


    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        
        # post = Posts.objects.create(**validated_data)

        post = super().create(validated_data = validated_data)

        if photos_data is not None:
            arr = []
            for photo_data in photos_data:
                photo_srl = PhotoSerializers2(data = {'file': photo_data, 'post': post.id})
                photo_srl.is_valid(raise_exception=True)  # Вызываем валидацию
                photo_srl.save(post=post)
                arr.append(photo_srl.data)

        return post



    def update(self, instance, validated_data):
        photos_data = validated_data.pop('photos', None)

        if validated_data['method'] == "PUT":
            super().update(instance, validated_data)
            instance.photos.all().delete() 
            if photos_data is not None:
                arr = []
                for photo_data in photos_data:
                    photo_srl = PhotoSerializers2(data={'file': photo_data, 'post': instance.id})
                    photo_srl.is_valid(raise_exception=True)  
                    photo_srl.save(post=instance)  
                    arr.append(photo_srl.data)

        else:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            if photos_data is not None:
                instance.photos.all().delete() 
                arr = []
                for photo_data in photos_data:
                    photo_srl = PhotoSerializers2(data={'file': photo_data, 'post': instance.id})
                    photo_srl.is_valid(raise_exception=True)  
                    photo_srl.save(post=instance)  
                    arr.append(photo_srl.data)

        return instance
    
    # def update(self, instance, validated_data):
    #     raise_errors_on_nested_writes('update', self, validated_data)
    #     info = model_meta.get_field_info(instance)

    #     # Simply set each attribute on the instance, and then save it.
    #     # Note that unlike `.create()` we don't need to treat many-to-many
    #     # relationships as being a special case. During updates we already
    #     # have an instance pk for the relationships to be associated with.
    #     m2m_fields = []
    #     for attr, value in validated_data.items():
    #         if attr in info.relations and info.relations[attr].to_many:
    #             m2m_fields.append((attr, value))
    #         else:
    #             setattr(instance, attr, value)

    #     instance.save()

    #     # Note that many-to-many fields are set after updating instance.
    #     # Setting m2m fields triggers signals which could potentially change
    #     # updated instance and we do not want it to collide with .update()
    #     for attr, value in m2m_fields:
    #         field = getattr(instance, attr)
    #         field.set(value)

    #     return instance














# class PostSerializer(serializers.ModelSerializer):
#     videos = VideoSerializers2(many=True, required=False)
#     photos = PhotoSerializers2(many=True, required=False)
#     documents = DocumentSerializers2(many=True, required=False)

#     class Meta:
#         model = Posts
#         fields = ('id', 'created_date', 'modified_date', 'chat', 'text', 'videos', 'photos', 'documents')
#         read_only_fields = ('created_date', 'modified_date')

    # def create(self, validated_data):
    #     videos_data = validated_data.pop('videos', [])
    #     photos_data = validated_data.pop('photos', [])
    #     documents_data = validated_data.pop('documents', [])

    #     post = Posts.objects.create(**validated_data)

    #     self._create_or_update_related_objects(post, videos_data, Video)
    #     self._create_or_update_related_objects(post, photos_data, Photo)
    #     self._create_or_update_related_objects(post, documents_data, Document)

    #     return post

    # def update(self, instance, validated_data):
    #     videos_data = validated_data.pop('videos', [])
    #     photos_data = validated_data.pop('photos', [])
    #     documents_data = validated_data.pop('documents', [])

    #     instance.chat = validated_data.get('chat', instance.chat)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.save()

    #     request_method = self.context['request'].method
    #     if request_method == 'PUT':
    #         self._handle_put_related_objects(instance, videos_data, Video)
    #         self._handle_put_related_objects(instance, photos_data, Photo)
    #         self._handle_put_related_objects(instance, documents_data, Document)
    #     else:
    #         self._create_or_update_related_objects(instance, videos_data, Video)
    #         self._create_or_update_related_objects(instance, photos_data, Photo)
    #         self._create_or_update_related_objects(instance, documents_data, Document)

    #     return instance

    # def _create_or_update_related_objects(self, post, related_data, model_class):
    #     """
    #     Создает или обновляет связанные объекты (видео, фото, документы).
    #     """
    #     for data in related_data:
    #         obj_id = data.get('id')
    #         if obj_id:
    #             # Обновление существующего объекта
    #             obj_instance = model_class.objects.filter(id=obj_id, post=post).first()
    #             if obj_instance:
    #                 for attr, value in data.items():
    #                     setattr(obj_instance, attr, value)
    #                 obj_instance.save()
    #             else:
    #                 model_class.objects.create(post=post, **data)
    #         else:
    #             # Создание нового объекта
    #             model_class.objects.create(post=post, **data)

    # def _handle_put_related_objects(self, post, related_data, model_class):
    #     """
    #     Обрабатывает логику для PUT-запросов, удаляя отсутствующие объекты.
    #     """
    #     if not related_data:
    #         model_class.objects.filter(post=post).delete()
    #     else:
    #         existing_ids = {item.get('id') for item in related_data if item.get('id')}
    #         model_class.objects.filter(post=post).exclude(id__in=existing_ids).delete()
    #         self._create_or_update_related_objects(post, related_data, model_class)
