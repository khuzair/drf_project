from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from api.models import Student
from restAuthApi.serializers import StudentModelSerialiser
from .customThrotle import MyCustomRandomThrotle
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


class StudentThrottleModelView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser
    throttle_classes = [MyCustomRandomThrotle, UserRateThrottle]


# extends GenericAPIView and ListModelMixin
class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser
    authentication_classes = [SessionAuthentication]
    permission_classes  = [IsAuthenticated]
    throttle_classes = [MyCustomRandomThrotle, UserRateThrottle]
    


# extends GenericAPIView and RetrieveModelMixin
class StudentRetrieveApi(RetrieveAPIView):     
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'detail_stu'


# extends GenericAPIView and CreateModelMixin
class StudentCreateApi(CreateAPIView):
    serializer_class = StudentModelSerialiser


# extends GenericAPIView and UpdateModelMixin
class StudentUpdateApi(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser


# extends GenericAPIView and DestroyModelMixin
class StudentDeleteApi(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialiser
