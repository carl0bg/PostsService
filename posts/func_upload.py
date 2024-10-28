import os
import uuid

from django.utils import timezone



def get_path_upload_format(post, file):
    '''
    универсальный путь изображения
    '''
    end_extention = file.name.split(".")[-1] #забираем расширение
    file.name = str(uuid.uuid4().int) + "_" + str(post.id) + "." + end_extention
    return file
