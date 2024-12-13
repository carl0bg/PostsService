from pathlib import Path
from config.db_const import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.django_key

AUTH_USER_MODEL = 'TestUser.User'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_BASE_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_yasg',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'mptt'
]


PROJECT_APPS = [
    'posts',
    'photo',
    'video',
    'document',
    'TestUser',
    'JWT',
    'comments',
    'followers',
    'wall',
]

INSTALLED_APPS = DJANGO_BASE_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',  #управляет сеансами по запросам.
    # 'PostsService.middleware.JWTAuthenticationMiddleware', #my middleware for token
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',  #связывает пользователей с запросами с помощью сеансов. 
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'PostsService.middleware.HeaderCheckMiddleware',
]

ROOT_URLCONF = 'PostsService.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PostsService.wsgi.application'



DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': config.db_name,
    'USER': config.db_user,
    'PASSWORD': config.db_password,
    'HOST': config.db_host,
    'PORT': config.db_port,
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





#настройки storage minio
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = "django_minio_backend.models.MinioBackend"


AWS_ACCESS_KEY_ID = config.aws_access_key_id
AWS_SECRET_ACCESS_KEY = config.aws_secret_access_key
# AWS_S3_ENDPOINT_URL = 'http://minio:9000'
AWS_S3_ENDPOINT_URL = config.aws_s3_endpoint_url



DOCUMENT_BUCKET_NAME = config.aws_storage_bucket_name_document
VIDEO_BUCKET_NAME = config.aws_storage_bucket_name_video
PHOTO_BUCKET_NAME = config.aws_storage_bucket_name_photo

# Определите URL для каждого бакета
AWS_S3_DOCUMENT_URL = f'{AWS_S3_ENDPOINT_URL}/{DOCUMENT_BUCKET_NAME}/'
AWS_S3_VIDEO_URL = f'{AWS_S3_ENDPOINT_URL}/{VIDEO_BUCKET_NAME}/'
AWS_S3_PHOTO_URL = f'{AWS_S3_ENDPOINT_URL}/{PHOTO_BUCKET_NAME}/'
   
AWS_S3_FILE_OVERWRITE = False  # Не перезаписывать файлы с одинаковыми именами




REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer', #необходимо закоментировать на релиз, когда платформа drf не была видна, а только сырой json
    ],

    # # "DEFAULT_PERMISSION_CLASSES": [
    # #     'rest_framework.permissions.AllowAny',
    # # ],
    # "DEFAULT_AUTHENTICATION_CLASSES": (
    #     # 'rest_framework.authentication.TokenAuthentication',
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    #     # 'rest_framework.authentication.BasicAuthentication',

    # ),

    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'JWT.JWTAuthentication.JWTAuthentication',
    ),

    # "DEFAULT_SCHEMA_CLASS": 'rest_framework.schemas.coreapi.AutoSchema', #openapi #coreapi

    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',#это значит что доступ будет разрешен, только зарегистрированным пользователям
        'rest_framework.permissions.AllowAny',
    ],

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],

}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}



#jwt
JWS_SECRET_ACCESS_KEY = config.jws_secret_access_key



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logging/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


CORS_ALLOW_ALL_ORIGINS = True #TODO