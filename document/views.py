from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import DocumentSerializers
from .models import Document


class DocumentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializers




class DocumentListView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializers

    parser_classes = [MultiPartParser, FormParser]