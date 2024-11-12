from django.urls import path

from .views import ListFollowerView, AddFollowerView



# urlpatterns = [
#     path('comment', views.CommentsView.as_view({'post': 'create'})),
#     path('comment/<int:pk>', views.CommentsView.as_view({'put': 'update', 'delete': 'destroy'})),
#     path('post', views.PostView.as_view({'post': 'create'})),
#     path('post/<int:pk>', views.PostView.as_view({
#         'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
#     })),
#     path('post/user/<int:pk>', views.PostListView.as_view()),
# ]


urlpatterns = [
    path('<int:pk>', AddFollowerView.as_view()),
    path('', ListFollowerView.as_view()),
    # path('', ListFollowerView.as_view(), name='followers-list'),
]
