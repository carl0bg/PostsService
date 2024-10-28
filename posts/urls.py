from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'posts_api'


urlpatterns = [

    path('posts', PostListAPIView.as_view(), name='post_list'),
    path('posts/<int:pk>', PostGetOneAPIView.as_view(), name='post_get_one'),
    path('posts/create', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
]