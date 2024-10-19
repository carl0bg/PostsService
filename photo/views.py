from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse

from .serializers import PhotoSerializers
from .models import Photo


class PhotoDetailView(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers




class PhotoListView(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers

    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




def modify_input_for_multiple_files(post, image):
    dict = {}
    dict['post'] = post
    dict['file'] = image
    return dict



class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_images = Photo.objects.all()
        serializer = PhotoSerializers(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)


    def modify_input_for_multiple_files(post, image):
        dict = {}
        dict['post'] = post
        dict['file'] = image
        return dict


    def post(self, request, *args, **kwargs):
        post = request.data['post']

        images = dict((request.data).lists())['file']
        arr = []
        try:
            for img_name in images:
                modified_data = modify_input_for_multiple_files(post, img_name)
                file_serializer = PhotoSerializers(data=modified_data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    arr.append(file_serializer.data)

            return Response(arr, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)