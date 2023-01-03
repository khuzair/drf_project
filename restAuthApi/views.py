from winreg import HKEY_LOCAL_MACHINE
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render
from rest_framework import viewsets

from api import serializers
from .serializers import (
    StudentModelSerialiser, CustomUserRegistrationModelSerializer, 
    CustomUserLoginModelSerializer, UserProfileModelSerializer,
    UserChangePasswordModelSerializer, UserSendResetPasswordEmailModelSerializer,
    UserPasswordResetConfirmModelSerializer
)
from api.models import Student
from rest_framework.permissions import (
                        IsAuthenticated, 
                        AllowAny, IsAdminUser,
                        IsAuthenticatedOrReadOnly,
                        DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
)
from .permissions import MyCustomPermission
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .custom_authentication import MyCustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .custom_renderers import MyCustomRenderer
from rest_framework_simplejwt.tokens import RefreshToken



# generate custom token from simple jwt third party package 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class CustomUserRegistrationView(APIView):
    renderer_classes = [MyCustomRenderer]
    def post(self, requset, format=None):
        serializer = CustomUserRegistrationModelSerializer(data=requset.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'user': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLoginView(APIView):
    def post(self, request, format=None):
        serializer = CustomUserLoginModelSerializer(data=request.data)

        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)

        # if serializer not valid raise_exception occurs
        if serializer.is_valid(raise_exception=True): 
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_error': ['username or password field may be inncorrect']}},
                        status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class UserChangePasswordView(APIView):
    renderer_classes = [MyCustomRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordModelSerializer(data=request.data, context={
                'user': request.user
            })
        if serializer.is_valid(raise_exception=True):
            return Response({'user': 'password changed successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSendResetPasswordEmailView(APIView):
    renderer_classes = [MyCustomRenderer]

    def post(self, request, format=None):
        serializer = UserSendResetPasswordEmailModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password reset link has been sent to your email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetConfirmView(APIView):
    renderer_classes = [MyCustomRenderer]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetConfirmModelSerializer(data=request.data, context={
            'uid': uid, 
            'token': token
        })
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password has been reset successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    renderer_classes = [MyCustomRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileModelSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# allow APIs Authentication using SessionAuthentication and custom permissions
class StudentModelView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [MyCustomPermission, IsAuthenticated] # only register user can access the API also add custom permission
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser


# Grant api access using TokenAuthentication
class StudentApiView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser


# grant api access using custom authentication
class CustomAuthStudentApiView(viewsets.ModelViewSet):
    authentication_classes = [MyCustomAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser


# grant api access using third party api token authentication
class JWTAuthStudentApiView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def student_api_view(request, pk=None): # by default pk will be none
    if request.method == 'GET':
        id = request.data.get('id') # grab an id which you are trying to fetch in the database model instance
        if id is not None:
            stu = Student.objects.get(pk=id) # grab model object using their id
            serializer = StudentModelSerialiser(stu) # parse complex data into python data
            return Response(serializer.data, status=status.HTTP_200_OK) # convert python data into json format
        stu = Student.objects.all()
        serializer = StudentModelSerialiser(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentModelSerialiser(data=request.data) # convert json object into python data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data is created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentModelSerialiser(stu, data=request.data) # all field must be update
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)

    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentModelSerialiser(stu, data=request.data, partial=True) # some fields are allowed to be update
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data is deleted'}, status=status.HTTP_202_ACCEPTED)