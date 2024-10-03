from django.urls import path

from .view_v1 import RegistrationAPIView, LoginAPIView


app_name = 'auth'


urlpatterns = [
    path('user/register/', RegistrationAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),


]