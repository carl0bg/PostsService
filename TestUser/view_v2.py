from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import permission_classes



from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from JWT.view import TokenObtainPairView
from JWT.token import RefreshToken

from .serializers import LoginSerializer, RegistrationSerializer, LogoutSerializer
from .user_renderer import UserJSONRenderer
from .models import User



class RegistrationAPIView2(APIView):
    """
    Регстрация пользователей -> username, tokens 
    """
    serializer_class = RegistrationSerializer
    # parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]



    @swagger_auto_schema(
        operation_description="Registration",
        request_body= serializer_class,
        responses={201: serializer_class(many=False)}
    )
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user: User = serializer.save()
            tokens = TokenObtainPairView().post(request).data
            return Response({'username': user.username, 'tokens': tokens}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    





class LoginAPIView2(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    parser_classes = [JSONParser]

    @swagger_auto_schema(
        operation_description="Login",
        request_body= serializer_class,
        responses={201: serializer_class(many=False), 400: serializer_class()}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user: User = serializer.validated_data['user']
            tokens = TokenObtainPairView().post(request).data
            return Response({'username': user.username, 'tokens': tokens}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class LogoutAPIView(APIView):
    """
    Эндпоинт для разлогинивания пользователя
    """
    permission_classes = (AllowAny,)
    parser_classes = [JSONParser]
    serializer_class = LogoutSerializer
    

    @swagger_auto_schema(
        operation_description="Logout",
        request_body= serializer_class,
        responses={200: serializer_class(many=False)}
    )
    def post(self, request):
        try:
            token = request.data

            if RefreshToken.blacklist(RefreshToken(token['refresh'])):
                return Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)