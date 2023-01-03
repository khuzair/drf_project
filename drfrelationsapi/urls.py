from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongModelViewSet, SingerModelViewSet, SingerNestedModelViewSet

app_name = "drfrelationsapi"


router = DefaultRouter()

router.register('songapi', SongModelViewSet, basename="song")
router.register('singerapi', SingerModelViewSet, basename="singer")
router.register('singer_song', SingerNestedModelViewSet, basename="singer-song")


urlpatterns = [
    path('', include(router.urls)),
]