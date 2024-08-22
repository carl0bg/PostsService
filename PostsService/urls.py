from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger_url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls', namespace= 'posts_api'))
]

urlpatterns += swagger_url