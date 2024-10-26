from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'posts_api'



# router = DefaultRouter()
# router.register(r'posts', PostViewSet2)

# # router.register(r'posts', PostViewSet3_sets)


# urlpatterns = [
#     # path('post/<int:pk>/', PostDetailView.as_view(), name = 'one_post'),
#     # path('posts/', PostListView.as_view(), name = 'list_post'),


#     path('v2/', include(router.urls)),

#     # path('v3/', include(router.urls)),
#     # path('v3/ps/', ReviewCreateView3.as_view()),
#     # path("v3/posts/", PostsListView3.as_view()),
#     # path("v3/posts/<int:pk>/", PostsDetailView3.as_view()),

# ]


# router = DefaultRouter()
# router.register(r'posts', PostListCreateAPIView, basename='post')

urlpatterns = [
    # path('', include(router.urls)),

    path('posts', PostListAPIView.as_view(), name='post_list'),
    path('posts/<int:pk>', PostGetOneAPIView.as_view(), name='post_get_one'),
    path('posts/create', PostCreateAPIView.as_view(), name='post_create'),


    # path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
]