from django.urls import path, include
from .views import *



urlpatterns = [
    path('<int:pk>', WallView.as_view({'get': 'retrieve'})),
    path('', WallView.as_view({'get': 'list'})),
]