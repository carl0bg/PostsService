from rest_framework import serializers

from .models import Posts

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields= '__all__'



        