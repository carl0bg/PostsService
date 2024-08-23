from storages.backends.s3boto3 import S3Boto3Storage
import boto3

from PostsService.settings import DOCUMENT_BUCKET_NAME, PHOTO_BUCKET_NAME, VIDEO_BUCKET_NAME
from config.db_const import config


class DocumentStorage(S3Boto3Storage):
    bucket_name = DOCUMENT_BUCKET_NAME 

class VideoStorage(S3Boto3Storage):
    bucket_name = VIDEO_BUCKET_NAME 

class PhotoStorage(S3Boto3Storage):
    bucket_name = PHOTO_BUCKET_NAME 



def delete_type_from_s3(obj, bucket_name):
        s3_client = boto3.client(
            's3',
            aws_access_key_id=config.aws_access_key_id,
            aws_secret_access_key=config.aws_secret_access_key,
            endpoint_url=config.aws_s3_endpoint_url
        )
        key = obj.file.name

        try:
            s3_client.delete_object(Bucket=bucket_name, Key=key)
        except Exception as e:
            print(e)