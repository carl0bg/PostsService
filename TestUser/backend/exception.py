from rest_framework.exceptions import APIException




class TokenBackendError(Exception):
    pass


class TokenError(Exception):
    pass



class TokenCompError(APIException):
    status_code = 401
    default_detail = 'Given token not valid'
    default_code = 'Given token not valid'