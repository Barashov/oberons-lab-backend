from django.contrib.auth.backends import BaseBackend
from rest_framework import authentication
import jwt
from django.conf import settings
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request, **kwargs):

        auth_header = authentication.get_authorization_header(request).decode('utf-8').split()
        try:
            if len(auth_header) == 2 and auth_header[0] == 'Token':
                token = jwt.decode(auth_header[1],
                                   settings.SECRET_KEY,
                                   algorithms='HS256')

                user = User.objects.get(pk=token['id'])
                return user, token
            else:
                return

        except:
            return
