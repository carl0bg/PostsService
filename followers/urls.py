from django.urls import path

from .views import ListFollowerView, AddFollowerView, DeleteFollowerView, IsFollowerToView



urlpatterns = [
    path('sub/<int:pk>', AddFollowerView.as_view()),
    path('unsub/<int:pk>', DeleteFollowerView.as_view()),
    path('my_all', ListFollowerView.as_view()),
    path('sub_on', IsFollowerToView.as_view())

]
