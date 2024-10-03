from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger_url



urlpatterns = [
    # path('admin/', admin.site.urls),

    path('posts_api/', include('posts.urls', namespace= 'posts_api')),
    path('photo_api/', include('photo.urls', namespace= 'photo_api')),
    path('video_api/', include('video.urls', namespace= 'video_api')),
    path('document_api/', include('document.urls', namespace= 'document_api')),

    path('auth_api/', include('TestUser.urls', namespace='users_api')),
    path('token_api/', include('JWT.urls', namespace='token_api'))
]

urlpatterns += swagger_url