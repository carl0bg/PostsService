from django.urls import path

from .view import TokenObtainPairView, TokenRefreshView


app_name = 'token'


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]