from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'posts_api'



router = DefaultRouter()
# router.register(r'posts', PostViewSet2)

router.register(r'posts', PostViewSet3_sets)


urlpatterns = [
    # path('post/<int:pk>/', PostDetailView.as_view(), name = 'one_post'),
    # path('posts/', PostListView.as_view(), name = 'list_post'),


    # path('v2/', include(router.urls)),

    path('v3/', include(router.urls)),
    path('v3/ps/', ReviewCreateView3.as_view()),
    # path("v3/posts/", PostsListView3.as_view()),
    # path("v3/posts/<int:pk>/", PostsDetailView3.as_view()),

]