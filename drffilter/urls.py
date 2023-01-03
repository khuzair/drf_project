from django.urls import path, include
from .views import (
    PersonListApi, PersonCreateApi,
    PersonUpdateApi, PersonDeleteApi,
    PersonRetrieveApi
)

app_name = "drffilter"

urlpatterns = [

    path('person_list/', PersonListApi.as_view(), name="person-list"),
    path('person_list/<int:pk>/', PersonRetrieveApi.as_view(), name="person-detail"),
    path('person_create', PersonCreateApi.as_view(), name="person-create"),
    path('person_update/<int:pk>/', PersonUpdateApi.as_view(), name="person-update"),
    path('person_delete/<int:pk>/', PersonDeleteApi.as_view(), name="person-delete"),
    
]