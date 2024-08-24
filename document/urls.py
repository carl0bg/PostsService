from django.urls import path
from .views import *

app_name = 'document_api'

urlpatterns = [
    path('document/<int:pk>/', DocumentDetailView.as_view(), name = 'one_document'),
    path('documents/', DocumentListView.as_view(), name = 'list_document'),
]