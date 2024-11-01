from django.urls import path

from .view_v1 import RegistrationAPIView, LoginAPIView
from .view_v2 import *

app_name = 'auth'


urlpatterns = [
    # path('user/v1/register/', RegistrationAPIView.as_view()),
    # path('user/v1/login/', LoginAPIView.as_view()),

    path('user/v2/register/', RegistrationAPIView2.as_view()),
    path('user/v2/login/', LoginAPIView2.as_view()),
    path('user/v2/logout/', LogoutAPIView.as_view()),
]