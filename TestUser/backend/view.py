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


class InvalidToken():
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Token is invalid or expired"
    default_code = "token_not_valid"



class TokenError(Exception):
    pass






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
        # try:
        #     return import_string(self._serializer_class)
        # except ImportError:
        #     msg = "Could not import serializer '%s'" % self._serializer_class
        #     raise ImportError(msg)

    def get_authenticate_header(self, request: Request) -> str:
        return '{} realm="{}"'.format(
            'Bearer',
            self.www_authenticate_realm,
        )

    @swagger_auto_schema(
        operation_description="Token_access_refresh",
        request_body= serializer_class,
        responses={201: serializer_class(many=False)}
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])


        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenViewBase): #use
    """
    return access and refresh JSON 
    """
    # serializer_class = MyTokenObtainPairSerializer
    _serializer_class = TokenObtainPairSerializer


token_obtain_pair = TokenObtainPairView.as_view()


class TokenRefreshView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """

    _serializer_class = TokenRefreshSerializer


token_refresh = TokenRefreshView.as_view()

