
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class MyCustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # grab username whome you have mentioned in urls
        username = request.GET.get('username') 
        if username is None:
            return None

        try:
            # match the username from database username
            user = User.objects.get(username=username)

        except user.DoesNotExist:
            raise AuthenticationFailed('No such user')

        return (user, None)
        