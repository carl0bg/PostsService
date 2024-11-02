from django.urls import path

from .view_v1 import RegistrationAPIView, LoginAPIView
from .view_v2 import *

app_name = 'auth'


urlpatterns = [
    path('user/v2/register/', RegistrationAPIView2.as_view()),
    path('user/v2/login/', LoginAPIView2.as_view()),
    path('user/v2/logout/', LogoutAPIView.as_view()),

    path('user/profile/<int:pk>', UserNetView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('user/<int:pk>', UserNetPublicView.as_view({'get': 'retrieve'})),

]