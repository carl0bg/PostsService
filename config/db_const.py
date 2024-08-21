from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_host: str
    db_user: str
    db_password: str
    db_port: int
    db_name: str
    django_key: str
    aws_storage_bucket_name: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_s3_endpoint_url: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()