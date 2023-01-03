from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import StudentThrottleModelView
from rest_framework.routers import DefaultRouter
from .views import StudentCreateApi, StudentListApi, StudentDeleteApi, StudentRetrieveApi, StudentUpdateApi


app_name = "restthrotapi"


router = DefaultRouter()
router.register('throtle', StudentThrottleModelView, basename="throtle")

urlpatterns = [
    # url for model view set
    path('student/', include(router.urls)),

    # url for generic api view
    path('student_list/',StudentListApi.as_view(), name="student-list"),
    path('student_list/<int:pk>/',StudentRetrieveApi.as_view(), name="student-retrieve"),
    path('student_create/',StudentCreateApi.as_view(), name="student-create"),
    path('student_update/<int:pk>/',StudentUpdateApi.as_view(), name="student-Update"),
    path('student_delete/<int:pk>/',StudentDeleteApi.as_view(), name="student-delete"),
]