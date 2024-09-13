from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import RegistrationSerializer



class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    parser_classes = [MultiPartParser, FormParser]



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