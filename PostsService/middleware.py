from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

import jwt

class HeaderCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем наличие нужного заголовка
        if '2003' not in request.headers:
            return HttpResponseForbidden("Access denied: Missing header")

        # Продолжаем обработку запроса
        response = self.get_response(request)
        return response


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Извлекаем токен из заголовка
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return JsonResponse({'error': 'Authorization header is expected'}, status=401)

        try:
            # Убедитесь, что токен начинается с "Bearer "
            if not auth_header.startswith('Bearer '):
                return JsonResponse({'error': 'Invalid authorization header format'}, status=401)

            # Извлекаем токен
            token = auth_header.split(' ')[1]

            # Проверяем и декодируем токен
            payload = jwt.decode(token, 'dimas', algorithms=['HS256'])

            # Вы можете добавить объект пользователя в request, если это необходимо
            request.user_id = payload.get('user_id')  # Предполагается, что в токене есть поле user_id
            # Дополнительная логика для поиска пользователя в БД и добавления его в request
            if request.user_id == '1':
                print('Nicccccccccccceee')
            else:
                print("Nooooooooooooooo")

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)