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
    photos = PhotoSerializers2(many = True, required=False)
    videos = VideoSerializers2(many = True, required=False)


    class Meta:
        model = Posts
        fields = '__all__'


    def data_pars_sub(self, data_list, post, serializ):
        for photo_data in data_list:
            photo_srl = serializ(data = {'file': photo_data, 'post': post.id})
            photo_srl.is_valid(raise_exception=True)  
            photo_srl.save(post=post)



    def create(self, validated_data):
        photos_data = validated_data.pop('photos', None)
        documents_data = validated_data.pop('documents', None)
        videos_data = validated_data.pop('videos', None)

        post = super().create(validated_data)

        if photos_data is not None:
            self.data_pars_sub(photos_data, post, PhotoSerializers2)

        if documents_data is not None:
            self.data_pars_sub(documents_data, post, DocumentSerializers2)

        if videos_data is not None:
            self.data_pars_sub(videos_data, post, VideoSerializers2)

        return post


    def update(self, post, validated_data):
        photos_data = validated_data.pop('photos', None)
        documents_data = validated_data.pop('documents', None)
        videos_data = validated_data.pop('videos', None)

        if validated_data['method'] == "PUT":
            super().update(post, validated_data)
            post.photos.all().delete() 
            post.documents.all().delete() 
            post.videos.all().delete() 

            if photos_data is not None:
                self.data_pars_sub(photos_data, post, PhotoSerializers2)

            if documents_data is not None:
                self.data_pars_sub(documents_data, post, DocumentSerializers2)

            if videos_data is not None:
                self.data_pars_sub(videos_data, post, VideoSerializers2)
        else: #PATCH
            for attr, value in validated_data.items():
                setattr(post, attr, value)
            post.save()
            if photos_data is not None:
                post.photos.all().delete() 
                self.data_pars_sub(photos_data, post, PhotoSerializers2)
            if documents_data is not None:
                post.documents.all().delete() 
                self.data_pars_sub(documents_data, post, DocumentSerializers2)
            if videos_data is not None:
                post.videos.all().delete() 
                self.data_pars_sub(videos_data, post, VideoSerializers2)


        return post