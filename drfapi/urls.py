from argparse import Namespace
from email.mime import base
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from restAuthApi.views import StudentModelView, JWTAuthStudentApiView
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
    TokenVerifyView,
)


# create DefaultRouter object for api app
router = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()


# register StudentViewSet with router for api app
router.register('student_viewset_api', views.StudentViewSet, basename='student-viewset')
router2.register('student_modelviewset_api', views.StudentModelViewSet, basename='student-modelviewset-api'),
router3.register('student_readmodelviewset_api', views.StudentReadOnlyModelViewSet, basename='student-read-model-viewset-api')

# create DefaultRouter object for api restAuthpi
router4 = DefaultRouter()
# register StudentViewSet with router for restAuthApi app
router4.register('studentapi', StudentModelView, basename='student')



urlpatterns = [

    path('admin/', admin.site.urls),

    # url path for app_name 'api'
    path('student_api_view/', include(router.urls)),
    path('modelviewset/', include(router2.urls)),
    path('readmodelviewset/', include(router3.urls)),
    path('api/', include('api.urls', namespace='api')),

    path('rest_auth/', include('rest_framework.urls', namespace='rest_framework')), # provide login, logout facilty on the user.request page

    # url path for app_name 'restAuthApi'
    path('rest_auth_api/', include('restAuthApi.urls', namespace="restAuthApi")),
    path('gettoken/', obtain_auth_token),
    path('', include(router4.urls)),

    # url path for restthrotapi app
    path('rest_throat_api/', include('restthrotapi.urls', namespace="restthrotapi")),

    # url for drffilter app
    path('django_filter/', include('drffilter.urls', namespace="django-filter")),

    # url for drfpagination app
    path('pagination/', include('drfpagination.urls', namespace="pagination")),

    # url for drfrelationsapi app
    path('drf_relation_api/', include('drfrelationsapi.urls', namespace="drfrelationsapi")),
]



router7 = DefaultRouter()
router7.register('jwt_auth_view', JWTAuthStudentApiView, basename='jwt-auth-view')
# url token authentication from third party package

urlpatterns += [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # for generating token jwt
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # for refreshing token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # for verifying token
    path('api_auth/', include(router7.urls)),

]