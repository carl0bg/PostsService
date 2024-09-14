from django.urls import path

from .views import RegistrationAPIView, LoginAPIView

app_name = 'auth'


urlpatterns = [
    path('users/register/', RegistrationAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),
]