from django.urls import path
from .views import *

app_name = 'posts_api'

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'one_post'),
    path('posts/', PostListView.as_view(), name = 'list_post'),
]