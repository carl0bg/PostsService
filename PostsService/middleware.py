from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.urls import resolve

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView


import jwt
# from jwt.exceptions import ExpiredSignatureError, InvalidTokenError, DecodeError

from TestUser.backend.JWTAuthentication import JWTAuthentication
from config.db_const import config
from TestUser.models import User





class JWTAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.authenticator = JWTAuthentication()

    def __call__(self, request):
        # Получаем пользователя через класс аутентификации
        user = self.authenticator.authenticate(request)
        
        # Если пользователь не аутентифицирован, оставляем request.user пустым
        if not user:
            request.user = None

        # Разрешаем доступ к представлениям, где стоит AllowAny
        # if request.resolver_match:
            # view = request.resolver_match.func.cls
            # if hasattr(view, 'permission_classes'):
            #     # Если в разрешениях есть AllowAny, пропускаем запрос
            #     for permission in view.permission_classes:
            #         if permission.__name__ == 'AllowAny':
            #             return self.get_response(request)

        # Если пользователь не аутентифицирован и URL не имеет AllowAny, возвращаем ошибку
        # if not request.user:
        #     return JsonResponse({'detail': 'Требуется аутентификация'}, status=401)

        return self.get_response(request)
































# class JWTAuthenticationMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         # Извлекаем токен из заголовка
#         auth_header = request.META.get('HTTP_AUTHORIZATION')
#         if auth_header is None:
#             # return JsonResponse({'error': 'Authorization header is expected'}, status=401)
#             return True

#         try:
#             # Убедитесь, что токен начинается с "Bearer "
#             if not auth_header.startswith('Bearer '):
#                 return JsonResponse({'error': 'Invalid authorization header format'}, status=401)

#             # Извлекаем токен
#             token = auth_header.split(' ')[1]

#             # Проверяем и декодируем токен
#             payload = jwt.decode(token, config.jws_secret_access_key, algorithms=['HS256'])

#             # Вы можете добавить объект пользователя в request, если это необходимо
#             request.user_id = payload.get('user_id')  # Предполагается, что в токене есть поле user_id
#             # Дополнительная логика для поиска пользователя в БД и добавления его в request


#         except jwt.ExpiredSignatureError:
#             return JsonResponse({'error': 'Token has expired'}, status=401)
#         except jwt.InvalidTokenError:
#             return JsonResponse({'error': 'Invalid token'}, status=401)




# class JWTAuthenticationMiddleware(MiddlewareMixin):
#     # def process_request(self, request: WSGIRequest):
#     #     # Разрешаем доступ ко всем методам OPTIONS без проверки токена
#     #     if request.method == 'OPTIONS':
#     #         return None

#     #     # Извлечение класса представления (view), чтобы проверить его разрешения
#     #     # view_class = self.get_view_class(request)

#     #     # Проверка разрешений
#     #     if view_class:
#     #         view_permissions = self.get_permissions(view_class)
#     #         if any(isinstance(permission, AllowAny) for permission in view_permissions):
#     #             # Если разрешение AllowAny — доступ открыт без проверки токена
#     #             return None

#         # Извлекаем заголовок авторизации
#     auth_header = request.META.get('HTTP_AUTHORIZATION', '')

#         # Проверка наличия и формата заголовка
#     if not auth_header or not auth_header.startswith('Bearer '):
#         return JsonResponse({'error': 'Authorization header is missing or malformed'}, status=401)

#         token = auth_header.split(' ')[1]  # Извлечение токена

#         try:
#             # Декодирование токена
#             payload = jwt.decode(token, config.jws_secret_access_key, algorithms=['HS256'])

#             # Проверка, что в payload есть user_id
#             if 'user_id' not in payload:
#                 return JsonResponse({'error': 'Invalid token payload: user_id is missing'}, status=401)

#             # Присваиваем user_id в request или получаем пользователя
#             user_id = payload['user_id']

#             # Здесь можно добавить логику для поиска пользователя в БД
#             user = User.objects.get(id=user_id)
#             request.user = user

#         except ExpiredSignatureError:
#             return JsonResponse({'error': 'Token has expired'}, status=401)
#         except (InvalidTokenError, DecodeError):
#             return JsonResponse({'error': 'Invalid token'}, status=401)
#         except Exception as e:
#             return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

#     # def get_view_class(self, request: WSGIRequest):
#     #     """
#     #     Получаем класс представления, связанный с запросом.
#     #     """
#     #     # Используем резолвер URL, чтобы найти соответствующее view
#     #     resolver_match = resolve(request.path_info).url_name
#     #     if resolver_match:
#     #         return resolver_match.func.view_class
#     #     return None



#     def get_view_class(self, request: WSGIRequest):
#         """
#         Получаем класс представления, связанный с запросом.
#         """
#         # Используем резолвер URL, чтобы найти соответствующее представление
#         resolver_match = resolve(request.path_info)
        
#         # Проверяем, есть ли у функции атрибут `view_class`
#         if hasattr(resolver_match.func, 'view_class'):
#             return resolver_match.func.view_class
        
#         # Возвращаем None, если не удается найти класс представления
#         return None

#     def get_permissions(self, view_class):
#         """
#         Возвращаем разрешения, определенные для представления.
#         """
#         # Если view наследует от APIView, получаем его разрешения
#         if issubclass(view_class, APIView):
#             return view_class.permission_classes
#         return []