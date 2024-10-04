from rest_framework import serializers
from django.contrib.auth import authenticate


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


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)

#     def validate(self, data):

#         username = data.get('username', None)
#         password = data.get('password', None)


#         # Вызвать исключение, если не предоставлена почта.
#         if username is None:
#             raise serializers.ValidationError(
#                 'An username is required to log in.'
#             )

#         # Вызвать исключение, если не предоставлен пароль.
#         if password is None:
#             raise serializers.ValidationError(
#                 'A password is required to log in.'
#             )

#         user = authenticate(username=username, password=password)

#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this username and password was not found.'
#             )

#         if not user.is_active:  # TODO
#             raise serializers.ValidationError(
#                 'This user has been deactivated.'
#             )

#         return {
#             'username': user.username,
#             'token': user.token
#         }