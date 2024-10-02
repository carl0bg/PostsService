from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import permission_classes



from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import LoginSerializer, RegistrationSerializer
from .user_renderer import UserJSONRenderer



@permission_classes([AllowAny])
class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    # permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    parser_classes = [MultiPartParser, FormParser]
    # renderer_classes = (UserJSONRenderer)


    @swagger_auto_schema(
        operation_description="Registration",
        manual_parameters=[
            openapi.Parameter(
                'username',
                openapi.IN_FORM,
                description="username",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                'password',
                openapi.IN_FORM,
                description="password",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
        responses={201: serializer_class(many=False)}
    )
    def post(self, request, *args, **kwargs):

        user = request.data 

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    



class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer
    # parser_classes = [MultiPartParser, FormParser]
    parser_classes = [JSONParser]



    @swagger_auto_schema(
        operation_description="Login",
        request_body= serializer_class,
        responses={201: serializer_class(many=False)}
    )
    def post(self, request, *args, **kwargs):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    