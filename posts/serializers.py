from rest_framework import serializers

from .models import Posts, Photo, Document, Video

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields= '__all__'


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields= '__all__'

        
class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields= '__all__'

        
class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields= '__all__'

        