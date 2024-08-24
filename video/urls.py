from django.urls import path
from .views import *

app_name = 'video_api'

urlpatterns = [
    path('video/<int:pk>/', VideoDetailView.as_view(), name = 'one_video'),
    path('videos/', VideoListView.as_view(), name = 'list_video'),
]