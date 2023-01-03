from multiprocessing import context
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # grab user credintials
        serializer = self.serializer_class(data=request.data, context={'request': request})
        # check it is valid
        serializer.is_valid(raise_exception=True)
        # grab user data
        user = serializer._validated_data['user']
        # generate token if user have token key, else return token 
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.email
        })