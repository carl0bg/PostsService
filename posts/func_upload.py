import uuid


def get_path_upload_format(post, file):
    '''
    универсальный путь файла для minio
    '''
    end_extention = file.name.split(".")[-1] #забираем расширение
    file.name = str(uuid.uuid4()) + "_" + str(post.id) + "." + end_extention
    return file
