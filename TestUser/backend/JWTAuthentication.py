import jwt

from rest_framework import authentication, exceptions

from PostsService.settings import JWS_SECRET_ACCESS_KEY
from TestUser.models import User






class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header or len(auth_header) == 0:
            return None

        if len(auth_header) == 1:
            raise exceptions.AuthenticationFailed('Неполный заголовок аутентификации. Ожидается формат: "Bearer <token>"')

        if len(auth_header) > 2:
            raise exceptions.AuthenticationFailed('Некорректный заголовок аутентификации. Должно быть только два элемента.')

        # Декодируем префикс и токен
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            raise exceptions.AuthenticationFailed(f'Неправильный префикс: ожидается "{auth_header_prefix}"')

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            # Декодирование JWT
            payload = jwt.decode(token, JWS_SECRET_ACCESS_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Токен истек.')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Ошибка аутентификации. Невозможно декодировать токен.')

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Пользователь, соответствующий данному токену, не найден.')
        
        if not user.is_active:
            raise exceptions.AuthenticationFailed('Данный пользователь деактивирован.')

        return (user, token)