from django.urls import path
from . import views


urlpatterns = [
    path('new', views.CommentsView.as_view({'post': 'create'})),
    path('<int:pk>', views.CommentsView.as_view({'put': 'update', 'delete': 'destroy'})),
#     path('post', views.PostView.as_view({'post': 'create'})),
#     path('post/<int:pk>', views.PostView.as_view({
#         'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
#     })),
]