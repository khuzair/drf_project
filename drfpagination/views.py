from unicodedata import name
from drffilter.serializers import PersonModelSerializer
from drffilter.models import Person
from .custom_pagination import MyCustomePageNumberPagination, MyCustomLimitOffesetPagination, MyCustomCursonPagination
from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveAPIView, UpdateAPIView,
    DestroyAPIView
)




# extends GenericAPIView and ListModelMixin
class PersonListApi(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    # pagination_class = MyCustomePageNumberPagination
    # pagination_class = MyCustomLimitOffesetPagination
    pagination_class = MyCustomCursonPagination



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

