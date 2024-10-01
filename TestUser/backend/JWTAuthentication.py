import jwt

from rest_framework import authentication, exceptions, status


from PostsService.settings import JWS_SECRET_ACCESS_KEY
from TestUser.backend.exception import InvalidToken, TokenCompError, TokenError
from TestUser.models import User
from .token import Token, AccessToken



from django.contrib.auth import get_user_model

from rest_framework.request import Request

from typing import Optional, Set, Tuple, TypeVar





class JWTAuthentication(authentication.BaseAuthentication):


    www_authenticate_realm = "api"
    media_type = "application/json"
    auth_header_type_bytes = b'Bearer'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_model = get_user_model()

    def authenticate(self, request: Request) -> Optional[Tuple[User, Token]]:
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token



    def get_header(self, request: Request) -> bytes:
        '''return b'token'''
        header = request.META.get('HTTP_AUTHORIZATION')

        if isinstance(header, str):
            # Work around django test client oddness
            header = header.encode()

        return header

    def get_raw_token(self, header: bytes) -> Optional[bytes]:
        """
        Доп проверки, return token (непроверенный)
        """
        parts = header.split()

        if len(parts) == 0:
            return None

        if parts[0] not in self.auth_header_type_bytes:
            raise TokenCompError()

        if len(parts) != 2:
            raise TokenCompError()

        return parts[1]

    def get_validated_token(self, raw_token: bytes) -> Token:
        """
        Проверка токена 
        """
        try:
            return AccessToken(raw_token)
        except TokenError as e: 
            raise TokenCompError
        

    def get_user(self, validated_token: Token) -> User:
        '''
        Получения пользователя по id
        '''
        try:
            user_id = validated_token['id']
        except KeyError:
            raise InvalidToken()

        try:
            user = self.user_model.objects.get(**{'id': user_id})
        except self.user_model.DoesNotExist:
            raise InvalidToken(detail='Пользователь с указанным id не найден в базе данных')

        if not user.is_active:
            raise InvalidToken(detail= 'Пользователь неактивен')
        
        return user




def default_user_authentication_rule(user: User) -> bool:
    return user is not None and user.is_active