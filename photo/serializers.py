from rest_framework import serializers

from .models import Photo


class PhotoSerializers(serializers.ModelSerializer):

    # file = serializers.ImageField()

    class Meta:
        model = Photo
        fields= ('id', 'file')