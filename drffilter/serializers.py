from dataclasses import fields
from rest_framework import serializers
from .models import Person


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'city']