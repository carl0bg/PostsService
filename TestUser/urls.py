from django.urls import path

from .views import RegistrationAPIView, LoginAPIView
from .backend.view import TokenObtainPairView, TokenRefreshView

app_name = 'auth'


urlpatterns = [
    path('user/register/', RegistrationAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]