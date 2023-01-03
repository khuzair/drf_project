from unicodedata import name
from .serializers import PersonModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Person
from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveAPIView, UpdateAPIView,
    DestroyAPIView
)




# extends GenericAPIView and ListModelMixin
# class PersonListApi(ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonModelSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['name']


# class PersonListApi(ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonModelSerializer
#     filter_backends = [OrderingFilter]
#     ordering_fields = ['name']


class PersonListApi(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'city']   


# extends GenericAPIView and RetrieveModelMixin
class PersonRetrieveApi(RetrieveAPIView):     
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    


# extends GenericAPIView and CreateModelMixin
class PersonCreateApi(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer


# extends GenericAPIView and UpdateModelMixin
class PersonUpdateApi(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer


# extends GenericAPIView and DestroyModelMixin
class PersonDeleteApi(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
