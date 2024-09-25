from django.utils.module_loading import import_string
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from drf_yasg.utils import swagger_auto_schema

from typing import Optional

from TestUser.backend.serializers import MyTokenObtainPairSerializer, TokenObtainPairSerializer, TokenRefreshSerializer

# from .authentication import AUTH_HEADER_TYPES
# from .exceptions import InvalidToken, TokenError
# from .settings import api_settings


class TokenViewBase(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    # serializer_class = Optional[MyTokenObtainPairSerializer]
    # serializer_class = None
    serializer_class = MyTokenObtainPairSerializer
    _serializer_class = ""

    www_authenticate_realm = "api"

    def get_serializer_class(self) -> Serializer:

        if self.serializer_class:
            return self.serializer_class
        try:
            return import_string(self._serializer_class)
        except ImportError:
            msg = "Could not import serializer '%s'" % self._serializer_class
            raise ImportError(msg)


    @swagger_auto_schema(
        operation_description="Token_access_refresh",
        request_body= serializer_class,
        responses={201: serializer_class(many=False)}
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except Exception as e: #TODO
            print(e)


        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenViewBase): #use
    """
    return access and refresh JSON 
    """
    serializer_class = MyTokenObtainPairSerializer
    _serializer_class = TokenObtainPairSerializer


token_obtain_pair = TokenObtainPairView.as_view()


class TokenRefreshView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """

    _serializer_class = TokenRefreshSerializer


token_refresh = TokenRefreshView.as_view()


# class TokenObtainSlidingView(TokenViewBase):
#     """
#     Takes a set of user credentials and returns a sliding JSON web token to
#     prove the authentication of those credentials.
#     """

#     _serializer_class = api_settings.SLIDING_TOKEN_OBTAIN_SERIALIZER


# token_obtain_sliding = TokenObtainSlidingView.as_view()


# class TokenRefreshSlidingView(TokenViewBase):
#     """
#     Takes a sliding JSON web token and returns a new, refreshed version if the
#     token's refresh period has not expired.
#     """

#     _serializer_class = api_settings.SLIDING_TOKEN_REFRESH_SERIALIZER


# token_refresh_sliding = TokenRefreshSlidingView.as_view()


# class TokenVerifyView(TokenViewBase):
#     """
#     Takes a token and indicates if it is valid.  This view provides no
#     information about a token's fitness for a particular use.
#     """

#     _serializer_class = api_settings.TOKEN_VERIFY_SERIALIZER


# token_verify = TokenVerifyView.as_view()


# class TokenBlacklistView(TokenViewBase):
#     """
#     Takes a token and blacklists it. Must be used with the
#     `rest_framework_simplejwt.token_blacklist` app installed.
#     """

#     _serializer_class = api_settings.TOKEN_BLACKLIST_SERIALIZER


# token_blacklist = TokenBlacklistView.as_view()
