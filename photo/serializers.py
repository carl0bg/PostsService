from rest_framework import serializers

from .models import Photo


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'file', 'post')

    # def create(self, validated_data):
    #     return Photo.objects.create(**validated_data)