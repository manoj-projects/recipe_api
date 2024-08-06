from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings

class Auth(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('Authorization')
        token = request.headers.get('Token')
        print(api_key)
        if not api_key:
            raise AuthenticationFailed('Authorization Is Mandatory.')
        elif api_key != 'EMIS_web@2024_api':
            raise AuthenticationFailed('Authorization Key is Invalid')
        
        if not token:
            raise AuthenticationFailed('Token Is Mandatory.')

        try:
            decoded_token = jwt.decode(token, 'ingDLMRuGe9UKHRNjs7cYckS2yul4lc3', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired.')
        except jwt.InvalidTokenError as e:
            raise AuthenticationFailed('Invalid token: {}'.format(str(e)))

        # Attach the decoded token details to the request object
        request.tokenDetails = decoded_token
        print(decoded_token)
        
        return None, None
