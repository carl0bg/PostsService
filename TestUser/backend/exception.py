from rest_framework.exceptions import APIException, AuthenticationFailed




class TokenBackendError(Exception):
    pass


class TokenError(Exception):
    pass



class TokenCompError(APIException):
    status_code = 401
    default_detail = 'Данный токен недействителен'
    default_code = "token_not_valid"


class InvalidToken(AuthenticationFailed):
    status_code = 401
    default_detail = "Token is invalid or expired"
    default_code = "token_not_valid"


