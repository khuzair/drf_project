from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SingerModelNestedSerializer, SongModelSerializer, SingerHyperlinkedModelSerializer 
from .models import Song, Singer


class SingerModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerHyperlinkedModelSerializer


class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer


class SingerNestedModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerModelNestedSerializer