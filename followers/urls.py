from django.urls import path

from .views import ListFollowerView, AddFollowerView



urlpatterns = [
    path('<int:pk>', AddFollowerView.as_view()),
    path('', ListFollowerView.as_view()),
]
