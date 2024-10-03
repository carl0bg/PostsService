from django.utils.module_loading import import_string
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from drf_yasg.utils import swagger_auto_schema

from typing import Optional, Union

from .serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from .exception import InvalidToken, ParsesError, TokenError






class TokenViewBase(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = None

    www_authenticate_realm = "api"


    def get_authenticate_header(self, request: Request) -> str:
        return '{} realm="{}"'.format(
            'Bearer',
            self.www_authenticate_realm,
        )


    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])


        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenViewBase): #use
    """
    return access and refresh JSON
    """
    serializer_class = TokenObtainPairSerializer

    @swagger_auto_schema(
        operation_description="Token_access_refresh",
        request_body= serializer_class,
        responses={201: serializer_class(many=False)}
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        # try:
        response = super().post(request, *args, **kwargs)
        # except Exception as msg_ex: 
            # raise ParsesError(detail=msg_ex)
        return response

        




class TokenRefreshView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.TokenRefreshSerializer
    """
    serializer_class = TokenRefreshSerializer


    @swagger_auto_schema(
        operation_description="Token_refresh",
        request_body= serializer_class,
        responses={201: serializer_class(many=False)}
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        # try:
        response = super().post(request, *args, **kwargs)
        # except Exception as msg_ex: 
            # raise ParsesError(detail=msg_ex)
        return response

        




