from typing import TYPE_CHECKING, Any, Dict, Optional, TypeVar
from datetime import datetime, timedelta
from uuid import uuid4
import jwt

from .models import BlacklistedToken
from TestUser.models import User 


from .sub_func import aware_utcnow, datetime_from_epoch, datetime_to_epoch
from .exception import TokenBackendError, TokenError
# from .back import TokenBackend


from config.db_const import config







class Token:

    token_type: Optional[str] = None
    life_time: Optional[timedelta] = None

    algorithm = 'HS256'
    secret_key = config.jws_secret_access_key 


    def __init__(self, token = None, verify: bool = True) -> None:  

        self.token = token
        self.current_time = aware_utcnow()


        if token is not None: 
            try:
                self.payload = self.decode()
            except TokenBackendError:
                raise TokenError("Токен недействителен или срок действия истек")

            if verify:
                self.verify() 
        else:
            # New token.
            self.payload = {'token_type': self.token_type} 

            self.set_exp(from_time=self.current_time, lifetime=self.life_time)
            self.set_iat(at_time=self.current_time)

            self.set_jti()

    def __repr__(self) -> str:
        return repr(self.payload)

    def __getitem__(self, key: str):
        return self.payload[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.payload[key] = value

    def __delitem__(self, key: str) -> None:
        del self.payload[key]


    
    def __contains__(self, key: str) -> Any:
        return key in self.payload



    def decode(self):
        try:
            return jwt.decode(
                jwt = self.token, 
                key = self.secret_key,
                algorithms= self.algorithm,                
            )
        except jwt.InvalidAlgorithmError as ex:
            raise TokenBackendError("Invalid algorithm specified") from ex
        except jwt.InvalidTokenError as ex:
            raise TokenBackendError("Token is invalid or expired") from ex

    def encode(self, payload: Dict[str, Any]) -> str:
        """
        Returns an encoded token for the given payload dictionary.
        """
        jwt_payload = payload.copy()


        token = jwt.encode(
            jwt_payload,
            self.secret_key,
            algorithm=self.algorithm,
        )
        if isinstance(token, bytes):
            return token.decode("utf-8")
        return token

    def verify(self):
        self.check_time() #проверка на истечение



    def check_time(self, current_time: Optional[datetime] = None) -> None:
        
        if current_time is None:
            current_time = self.current_time

        try:
            claim_value = self.payload['exp']
        except KeyError:
            raise TokenError("В токене отсутствует 'exp'")
        
        try:
            iat_value = self.payload['iat']
        except KeyError:
            raise TokenError("В токене отсутствует 'iat'")


        claim_value = datetime_from_epoch(claim_value) 
        iat_value = datetime_from_epoch(iat_value)

        if claim_value <= current_time:
            raise TokenError('Токен просрочен')
                                            

        


    def set_exp(self, from_time: Optional[datetime] = None, lifetime: Optional[timedelta] = None) -> None:
        '''Установка время истечения'''
        if from_time is None:
            from_time = self.current_time

        if lifetime is None:
            lifetime = self.lifetime

        self.payload['exp'] = datetime_to_epoch(from_time + lifetime)


    def set_iat(self, at_time: Optional[datetime] = None) -> None:
        '''время выдачи токена'''
        if at_time is None:
            at_time = self.current_time

        self.payload['iat'] = datetime_to_epoch(at_time)


    def set_jti(self) -> None:
        '''уникальный идентификатор токена'''
        self.payload['jti'] = uuid4().hex




    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.payload.get(key, default)


    @classmethod
    def for_user(cls, user):
        """
        Returns an authorization token for the given user that will be provided
        after authenticating the user's credentials.
        """

        user_id = getattr(user, 'id')

        if not isinstance(user_id, int):
            user_id = str(user_id)

        token = cls()
        token['id'] = user_id
        return token
    


    def __str__(self) -> str:
        """
        return a token as a base64
        """
        return self.encode(self.payload)


class AccessToken(Token):
    token_type = "access"
    lifetime = timedelta(minutes=5)




class RefreshToken(Token):
    token_type = "refresh"
    lifetime = timedelta(days=1)
    no_copy_claims = (
        'token_type',
        "exp",
        'jti',
        "jti",
    )
    access_token_class = AccessToken

    @property
    def access_token(self) -> AccessToken:
        access = self.access_token_class()

        access.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value

        return access
    

    def check_blacklist(self) -> None:
        jti = self.payload['jti']

        if BlacklistedToken.objects.filter(jti = jti).exists():
            raise TokenError("Token is blacklisted")
        else:
            return True


    def verify(self, *args, **kwargs):
        if self.check_blacklist(): #если токена нет в blacklist
            super().verify(*args, **kwargs)

    @classmethod
    def blacklist(self, refresh_token = None) -> BlacklistedToken:
        """
        Проверка токена в Blacklist
        """
        jti = self.payload["jti"]
        user_id = self.payload["id"]

        # Ensure outstanding token exists with given jti
        token, flag_create = BlacklistedToken.objects.get_or_create(
            jti=jti,
            defaults={
                'user': str(user_id),
                "jti": jti,
            },
        )

        return BlacklistedToken.objects.get_or_create(jti=jti)


    def verify(self):
        return self.check_time()



    @classmethod
    def for_user(cls, user: User):

        token = super().for_user(user)  
        return token
