from rest_framework import serializers
from django.contrib.auth import authenticate
from typing import Any, Dict

from JWT.models import BlacklistedToken
from JWT.token import RefreshToken


from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('Аккаунт деактивирован.')
            else:
                raise serializers.ValidationError('Неправильные учетные данные.')
        else:
            raise serializers.ValidationError('Должны быть предоставлены "username" и "password".')
        return data



# class LogoutSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         return BlacklistedToken.objects.create_user(**validated_data)


#     class Meta:
#         model = BlacklistedToken


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    # access = serializers.CharField(read_only=True)
    token_class = BlacklistedToken

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh"])

        RefreshToken.blacklist()
        self.token_class.objects.create()



