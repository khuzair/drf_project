from functools import partial
import io
from django.shortcuts import render
from .serializers import StudentSerializer, StudentModelSerializer
from .models import Student
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)
from rest_framework.generics import (
    GenericAPIView, ListAPIView, RetrieveAPIView,
    CreateAPIView, UpdateAPIView, DestroyAPIView,
    ListCreateAPIView, RetrieveUpdateAPIView,
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
)


# read operations (list-retrive) are allowed for unauthorized users in this viewset
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# class based crud operation Api using ModelViewSet class
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# class based Api using ViewSet class
class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        print('******List******')
        print('Basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail: ', self.detail)
        print('Suffix: ', self.suffix)
        print('Name: ', self.name)
        print('Description: ', self.description)
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print('********Retrive*******')
        print('Basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail: ', self.detail)
        print('Suffix: ', self.suffix)
        print('Name: ', self.name)
        print('Description: ', self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu) # convert model object into Python object
            return Response(serializer.data) # return model instance Data into json

    def create(self, request):
        print('********Create********')
        print('Basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail: ', self.detail)
        print('Suffix: ', self.suffix)
        print('Name: ', self.name)
        print('Description: ', self.description)
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print('********Update*******')
        print('Basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail: ', self.detail)
        print('Suffix: ', self.suffix)
        print('Name: ', self.name)
        print('Description: ', self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentModelSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        print('********Partial Update*********')
        print('Basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail: ', self.detail)
        print('Suffix: ', self.suffix)
        print('Name: ', self.name)
        print('Description: ', self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentModelSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        print('***********Delete********')
        print('Basename: ', self.basename)
        print('Action: ', self.action)
        print('Detail: ', self.detail)
        print('Suffix: ', self.suffix)
        print('Name: ', self.name)
        print('Description: ', self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'}, status=status.HTTP_204_NO_CONTENT)


# extends GenericAPIView and ListModelMixin
class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# extends GenericAPIView and RetrieveModelMixin
class StudentRetrieveApi(RetrieveAPIView):     
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# extends GenericAPIView and CreateModelMixin
class StudentCreateApi(CreateAPIView):
    serializer_class = StudentModelSerializer


# extends GenericAPIView and UpdateModelMixin
class StudentUpdateApi(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# extends GenericAPIView and DestroyModelMixin
class StudentDeleteApi(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# extends GenericAPIView and ListModelMixin and CreateModelMixin
class StudentListCreateApi(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# extends GenericAPIView and RetrieveModelMixin and UpdateModelMixin
class StudentRetrieveUpdateApi(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# extends GenericAPIView and RetrieveModelMixin and DestroyModelMixin
class StudentRetrieveDestroyApi(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# extends GenericAPIView and RetrieveModelMixin, UpdateModelMixin and DestroyModelMixin
class StudentRetrieveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# class based Api using GenericAPIView and mixins classes
class StudentListApiView(ListModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class based Api using GenericAPIView and mixins classes
class StudentRetrieveApiView(RetrieveModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# class based Api using GenericAPIView and mixins classes
class StudentCreateApiView(CreateModelMixin, GenericAPIView):
    serializer_class = StudentModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class based Api using GenericAPIView and mixins classes
class StudentUpdateApiView(UpdateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# class based Api using GenericAPIView and mixins classes
class StudentDeleteApiView(DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class based Api using APIView
class StudentApi(APIView):

    def get(self, request, pk=None, format=None):
        id = pk # grab an id from database model

        if id is not None:
            stu = Student.objects.get(pk=id) # grab model object using their id
            serializer = StudentModelSerializer(stu) # parse complex data into python data
            return Response(serializer.data, status=status.HTTP_200_OK) # convert python data into json format

        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentModelSerializer(data=request.data) # fetch data from post form and convert json object into python data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data is created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):

        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentModelSerializer(stu, data=request.data) # all field must be update
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentModelSerializer(stu, data=request.data, partial=True) # some fields are allowed to be update
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data is deleted'}, status=status.HTTP_202_ACCEPTED)


# function based api
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api_view(request, pk=None): # by default pk will be none
    if request.method == 'GET':
        id = request.data.get('id') # grab an id from database model
        if id is not None:
            stu = Student.objects.get(pk=id) # grab model object using their id
            serializer = StudentModelSerializer(stu) # parse complex data into python data
            return Response(serializer.data, status=status.HTTP_200_OK) # convert python data into json format
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many=True)
        response = {
            'message': 'Some Extra Useful Message',
            'data': {
                'leder': serializer.data
            }
        }
        return Response(response)

    if request.method == 'POST':
        serializer = StudentModelSerializer(data=request.data) # convert json object into python data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data is created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentModelSerializer(stu, data=request.data) # all field must be update
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)

    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentModelSerializer(stu, data=request.data, partial=True) # some fields are allowed to be update
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data is deleted'}, status=status.HTTP_202_ACCEPTED)


@method_decorator(csrf_exempt, name='dispatch')
class StudentApiView(View):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None) # if data has id it will fetch it otherwise None
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu) # convert model object into Python object
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')

            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *agrs, **kwargs):
        if request.method == 'POST':
            json_data = request.body # json data will store in a request body variable
            stream = io.BytesIO(json_data) # convery json data into bytes stream
            python_data = JSONParser().parse(stream) # convert data stream into python data
            serializer = StudentSerializer(data=python_data) # convert it python object into complex data
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'data is created'}
                json_data = JSONRenderer().render(res) # convert python data into json and respond shows onto the web page
                return HttpResponse(json_data, content_type='application/json') # response data onto web page
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            json_data = request.body # json data will store in a request body variable
            stream = io.BytesIO(json_data) # convery json data into bytes stream
            python_data = JSONParser().parse(stream) # convert data stream into python data
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=python_data, partial=True) # if some field are update then partial wil be set to True other it will be False
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'data is Updated'}
                json_data = JSONRenderer().render(res) # convert python data into json and respond shows onto the web page
                return HttpResponse(json_data, content_type='application/json') # response data onto web page
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            json_data = request.body # json data will store in a request body variable
            stream = io.BytesIO(json_data) # convery json data into bytes stream
            python_data = JSONParser().parse(stream) # convert data stream into python data
            id = python_data.get('id') # retrive id 
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg': 'data is deleted'}
            json_data = JSONRenderer().render(res) # convert python data into json and respond shows onto the web page
            return HttpResponse(json_data, content_type='application/json') # response data onto web page


@csrf_exempt # To passing csrf exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None) # if data has id it will fetch it otherwise None
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu) # convert model object into Python object
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body # json data will store in a request body variable
        stream = io.BytesIO(json_data) # convery json data into bytes stream
        python_data = JSONParser().parse(stream) # convert data stream into python data
        serializer = StudentSerializer(data=python_data) # convert it python object into complex data
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data is created'}
            json_data = JSONRenderer().render(res)  # convert python data into json and respond shows onto the web page
            return HttpResponse(json_data, content_type='application/json')  # response data onto web page
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


    if request.method == 'PUT':
        json_data = request.body # json data will store in a request body variable
        stream = io.BytesIO(json_data) # convery json data into bytes stream
        python_data = JSONParser().parse(stream) # convert data stream into python data
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True) # if some field are update then partial wil be set to True other it will be False
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data is Updated'}
            json_data = JSONRenderer().render(res) # convert python data into json and respond shows onto the web page
            return HttpResponse(json_data, content_type='application/json') # response data onto web page
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'DELETE':
        json_data = request.body # json data will store in a request body variable
        stream = io.BytesIO(json_data) # convery json data into bytes stream
        python_data = JSONParser().parse(stream) # convert data stream into python data
        id = python_data.get('id') # retrive id 
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'data is deleted'}
        json_data = JSONRenderer().render(res) # convert python data into json and respond shows onto the web page
        return HttpResponse(json_data, content_type='application/json') # response data onto web page


# for deserialization data or post data 
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body # json data will store in a request body variable
        stream = io.BytesIO(json_data) # convery json data into bytes stream
        python_data = JSONParser().parse(stream) # convert data stream into python data
        serializer = StudentSerializer(data=python_data) # convert it python object into complex data
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data is created'}
            json_data = JSONRenderer().render(res) # convert python data into json and respond shows onto the web page
            return HttpResponse(json_data, content_type='application/json') # response data onto web page
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        

@csrf_exempt
def student_update(request):
    if request.method == 'PUT':
        json_data = request.body # json data will store in a request body variable
        stream = io.BytesIO(json_data) # convery json data into bytes stream
        python_data = JSONParser().parse(stream) # convert data stream into python data
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True) # if some field are update then partial wil be set to True other it will be False
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data is Updated'}
            json_data = JSONRenderer().render(res) # convert python data into json and respond shows onto the web page
            return HttpResponse(json_data, content_type='application/json') # response data onto web page
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


def student_detail(request, pk):
    stu = Student.objects.get(id=pk) # Model object: fetching single student data
    serializer = StudentSerializer(stu) # it convert queryset into python object
    json_data = JSONRenderer().render(serializer.data) # convert python object into json type

    return HttpResponse(json_data, content_type='application/json') # load json data onto web page


# serialization for getting data
def student_list(request):
    queryset = Student.objects.all() # queryset of list of the student model
    serializer = StudentSerializer(queryset, many=True) # it convert queryset into python object
    return JsonResponse(serializer.data, safe=False) # safe will be false for non dict objects


@csrf_exempt
def student_delete(request):
    if request.method == 'DELETE':
        json_data = request.body # json data will store in a request body variable
        stream = io.BytesIO(json_data) # convery json data into bytes stream
        python_data = JSONParser().parse(stream) # convert data stream into python data
        id = python_data.get('id') # retrive id 
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'data is deleted'}
        json_data = JSONRenderer().render(res) # convert python data into json and respond shows onto the web page
        return HttpResponse(json_data, content_type='application/json')  # response data onto web page


def student_api_list(request):
    queryset = Student.objects.all() # queryset of list of the student model
    serializer = StudentSerializer(queryset, many=True) # it convert queryset into python object
    json_data = JSONRenderer().render(serializer.data) # convert python object into json type

    return HttpResponse(json_data, content_type='application/json')  # load json data onto web page