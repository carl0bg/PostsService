from django.urls import path, include
from .yasg import urlpatterns as swagger_url


urlpatterns = [
    path('postser/posts/', include('posts.urls', namespace= 'posts_api')),

    path('postser/auth/', include('TestUser.urls', namespace='users_api')),
    path('postser/token/', include('JWT.urls', namespace='token_api')),

    path('postser/comments/', include('comments.urls')),
    path('postser/v2/wall/', include('wall.urls')),
    path('postser/followers/', include('followers.urls')),
]

urlpatterns += swagger_url