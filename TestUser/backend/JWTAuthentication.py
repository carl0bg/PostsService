import jwt

from rest_framework import authentication, exceptions, status


from PostsService.settings import JWS_SECRET_ACCESS_KEY
from TestUser.models import User



from django.core.exceptions import PermissionDenied
from django.http import JsonResponse



class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):

        try:
            # Получаем заголовок Authorization
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return None  # Токен отсутствует, возвращаем None

            # Разделяем заголовок на префикс и токен
            auth_header = auth_header.split()
            if len(auth_header) != 2 or auth_header[0].lower() != self.authentication_header_prefix.lower():
                # raise exceptions.AuthenticationFailed('Неправильный формат заголовка аутентификации')
                return JsonResponse({'detail': 'Неправильный формат заголовка аутентификации'}, status=status.HTTP_400_BAD_REQUEST)

            token = auth_header[1]
            return self._authenticate_credentials(request, token)
        except Exception as e:
            return JsonResponse({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def _authenticate_credentials(self, request, token):
        try:
            # Декодирование JWT
            payload = jwt.decode(token, JWS_SECRET_ACCESS_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'detail': 'Токен истек'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return JsonResponse({'detail': 'Невалидный токен'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем существование пользователя
        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            return JsonResponse({'detail': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        if not user.is_active:
            return JsonResponse({'detail': 'Пользователь деактивирован'}, status=status.HTTP_403_FORBIDDEN)

        # Устанавливаем пользователя в запрос
        request.user = user

        return (user, token)