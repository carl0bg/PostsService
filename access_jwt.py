import jwt
import datetime

from config.db_const import config

# from PostsService.settings import JWS_SECRET_ACCESS_KEY

def create_access_token_jws(user_id = 1):
    secret_key = config.jws_secret_access_key  # Используйте ключ, который хранится в settings.py
    algorithm = 'HS256'
    
    # Определяем полезную нагрузку (payload)
    payload = {
        'user_id': user_id,  
        'exp': datetime.datetime.now() + datetime.timedelta(hours=1),  # Время жизни токена
        'iat': datetime.datetime.now()  # Время создания токена
    }

    access_token = jwt.encode(payload, secret_key, algorithm=algorithm)

    print(access_token)
    return access_token

create_access_token_jws()