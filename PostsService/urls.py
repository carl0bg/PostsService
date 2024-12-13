from django.urls import path, include
from .yasg import urlpatterns as swagger_url



urlpatterns = [
    path('posts/', include('posts.urls', namespace= 'posts_api')),

    path('auth/', include('TestUser.urls', namespace='users_api')),
    path('token/', include('JWT.urls', namespace='token_api')),

    path('comments/', include('comments.urls')),
    path('v2/wall/', include('wall.urls')),
    path('followers/', include('followers.urls')),
]

urlpatterns += swagger_url