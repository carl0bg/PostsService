import os

from django.utils import timezone








def get_path_upload_image(post, file):
    '''
    универсальный путь изображения
    '''
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split(".")[-1] #забираем расширение
    head = file.split(".")[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + "_" + time + "." + end_extention
    return file_name
