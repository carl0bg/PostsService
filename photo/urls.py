from django.urls import path
from .views import *

app_name = 'photo_api'

urlpatterns = [
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name = 'one_photo'),
    # path('photos/', PhotoListView.as_view(), name = 'list_photo'),

    path('photos/', ImageView.as_view())
]