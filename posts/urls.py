from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'posts_api'


urlpatterns = [

    # path('posts', PostListAPIView.as_view(), name='post_list'),
    path('<int:pk>', PostGetOneAPIView.as_view(), name='post_get_one'),
    path('create', PostCreateAPIView.as_view(), name='post_create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),

    path('user/public/<int:pk>', PostListViewPublic.as_view()),
    path('user/private/<int:pk>', PostListViewPrivate.as_view()),
]