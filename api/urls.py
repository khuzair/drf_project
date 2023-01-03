from django.urls import path
from .views import (        
    student_detail, student_list, student_create,
    student_update, student_delete, student_api,
    StudentApiView, StudentApi, StudentListApiView,
    StudentCreateApiView, StudentRetrieveApiView,
    StudentUpdateApiView, StudentDeleteApiView,
    student_api_view, StudentListApi, StudentCreateApi,
    StudentRetrieveApi, StudentUpdateApi, StudentDeleteApi,
    StudentListCreateApi, StudentRetrieveUpdateApi,
    StudentRetrieveDestroyApi, StudentRetrieveUpdateDestroyApi
                    )

app_name = "api"

urlpatterns = [


    # extends GenericAPIView and Mixins
    path('student_list_api/', StudentListApi.as_view(), name="student-list-api"),
    path('student_list_api/<int:pk>/', StudentRetrieveApi.as_view(), name="student-detail-api"),
    path('student_create_api/', StudentCreateApi.as_view(), name="student-create-api"),
    path('student_update_api/<int:pk>/', StudentUpdateApi.as_view(), name="student-update-api"),
    path('student_delete_api/<int:pk>/', StudentDeleteApi.as_view(), name="student-delete-api"),
    path('student_list_create_api/', StudentListCreateApi.as_view(), name="student-list-create-api"),
    path('student_retrieve_update_api/<int:pk>/', StudentRetrieveUpdateApi.as_view(), name="student-retrieve-update-api"),
    path('student_retrieve_destroy_api/<int:pk>/', StudentRetrieveDestroyApi.as_view(), name="student-retrieve-destroy-api"),
    path('student_retrieve_update_destroy_api/<int:pk>/', StudentRetrieveUpdateDestroyApi.as_view(), name="student-retrieve-update-destroy-api"),

    # class based Api using GenericAPIView and mixins classes
    path('student_list_api_view/', StudentListApiView.as_view(), name="student-list-api-view"),
    path('student_list_api_view/<int:pk>', StudentRetrieveApiView.as_view(), name="student-retrieve-api-view"),
    path('student_create_api_view/', StudentCreateApiView.as_view(), name="student-create-api-view"),
    path('student_update_api_view/<int:pk>/', StudentUpdateApiView.as_view(), name="student-update-api-view"),
    path('student_delete_api_view/<int:pk>/', StudentDeleteApiView.as_view(), name="student-delete-api-view"),

    # class based Api using APIView
    path('students_api_list/', StudentApi.as_view(), name="students-api-list"),
    path('students_api_list/<int:pk>/', StudentApi.as_view(), name="student-detail-api"),

    # function based api
    path('student_view_api/', student_api_view, name="student-view-api"), 
    path('student_view_api/<int:pk>/', student_api_view, name="student-view-api"),
    path('student_api_view/', StudentApiView.as_view(), name="student-api-view"),
    path('student_api/', student_api, name="student-api" ),
    path('students/', student_list, name="student-list"),
    path('create_student/', student_create, name="create-student"),
    path('student/<int:pk>/', student_detail, name="student-detail"),
    path('student_update/', student_update, name="student-update"),
    path('student_delete/', student_delete, name="student-delete"),
    
]