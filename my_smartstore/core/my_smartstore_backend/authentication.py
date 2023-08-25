from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from my_smartstore_backend.models import Token


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        print(str(token).split())
        if token:
            try:
                user = Token.objects.get(token=str(token).split()[1]).user
            except:
                raise exceptions.AuthenticationFailed('Unauthenticated user')
        else:
            user = None
        return user,None



