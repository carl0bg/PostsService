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

from .serializers import LoginSerializer, RegistrationSerializer
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
        responses={201: serializer_class(many=False)}
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
    permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser]
    serializer_class = LoginSerializer
    


    def post(self, request):
        try:
            token = request.auth

            # Блокируем токен (делаем его недействительным)
            # BlacklistedToken.objects.create(token=token)
            RefreshToken.blacklist(token['refresh'])

            return Response({'detail': 'Logout successful.'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)