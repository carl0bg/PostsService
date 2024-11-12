from rest_framework import serializers

from .models import Follower
from TestUser.serializers import UserByFollowerSerializers


class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserByFollowerSerializers(read_only = True)

    class Meta:
        model = Follower
        fields = ('subscriber',)

