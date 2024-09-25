import jwt

from rest_framework import authentication, exceptions, status


from PostsService.settings import JWS_SECRET_ACCESS_KEY
from TestUser.models import User
from .token import Token, AccessToken


from django.contrib.auth import get_user_model

from rest_framework.request import Request

from typing import Optional, Set, Tuple, TypeVar





class JWTAuthentication(authentication.BaseAuthentication):


    www_authenticate_realm = "api"
    media_type = "application/json"
    auth_header_type_bytes = 'Bearer'

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

    # def authenticate_header(self, request: Request) -> str:
    #     return '{} realm="{}"'.format(
    #         AUTH_HEADER_TYPES[0],
    #         self.www_authenticate_realm,
    #     )

    def get_header(self, request: Request) -> bytes:

        header = request.META.get('HTTP_AUTHORIZATION')

        if isinstance(header, str):
            # Work around django test client oddness
            header = header.encode()

        return header

    def get_raw_token(self, header: bytes) -> Optional[bytes]:
        """
        Extracts an unvalidated JSON web token from the given "Authorization"
        header value.
        """
        parts = header.split()

        if len(parts) == 0:
            return None

        if parts[0] not in self.auth_header_type_bytes:
            return None

        if len(parts) != 2:
            raise ("Authorization header must contain two space-delimited values") #TODO

        return parts[1]

    def get_validated_token(self, raw_token: bytes) -> Token:
        """
        Validates an encoded JSON web token and returns a validated token
        wrapper object.
        """
        messages = []
        try:
            return AccessToken(raw_token)
        # except TokenError as e:  #TODO
        #     messages.append(
        #         {
        #             "token_class": AuthToken.__name__,
        #             "token_type": AuthToken.token_type,
        #             "message": e.args[0],
        #         }
        #     )
        except Exception:
            print('Error')


        # raise InvalidToken(
        #     {
        #         "detail": _("Given token not valid for any token type"),
        #         "messages": messages,
        #     }
        # )

    def get_user(self, validated_token: Token) -> User:
        try:
            user_id = validated_token['user_id']
        except KeyError:
            # raise InvalidToken(_("Token contained no recognizable user identification"))
            ... #TODO

        try:
            user = self.user_model.objects.get(**{'id': user_id})
        except self.user_model.DoesNotExist:
            # raise AuthenticationFailed(_("User not found"), code="user_not_found")
            ...

        if not user.is_active:
            # raise AuthenticationFailed(_("User is inactive"), code="user_inactive")
            ...

        # if api_settings.CHECK_REVOKE_TOKEN: #TODO для отзывания  токена
        #     if validated_token.get(
        #         api_settings.REVOKE_TOKEN_CLAIM
        #     ) != get_md5_hash_password(user.password):
        #         raise AuthenticationFailed(
        #             _("The user's password has been changed."), code="password_changed"
        #         )

        return user




def default_user_authentication_rule(user: User) -> bool:
    return user is not None and user.is_active