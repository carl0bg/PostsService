from rest_framework import serializers

from .models import Video



        
class VideoSerializers(serializers.ModelSerializer):

    # file = serializers.FileField()

    class Meta:
        model = Video
        fields= ('id', 'file')
        