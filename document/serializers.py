from rest_framework import serializers

from .models import Document


        
        
class DocumentSerializers(serializers.ModelSerializer):

    # file = serializers.FileField()

    class Meta:
        model = Document
        fields= ('id', 'file')




        