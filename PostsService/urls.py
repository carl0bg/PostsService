from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger_url


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('posts_api/', include('posts.urls', namespace= 'posts_api')),
    path('photo_api/', include('photo.urls', namespace= 'photo_api')),
    path('video_api/', include('video.urls', namespace= 'video_api')),
    path('document_api/', include('document.urls', namespace= 'document_api')),

    path('auth_api/', include('TestUser.urls', namespace='users_api')),

    path('auth_api/v2/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth_api/v2/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += swagger_url