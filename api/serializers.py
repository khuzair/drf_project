from pyexpat import model
from wsgiref import validate
from rest_framework import serializers
from .models import Student


def starts_with_a(value):
    if value[0].lower() != 'a':
        return serializers.ValidationError('name should start with A')

    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_a])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # for creating data
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):

        # user provide data will be update on these fields
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError('seats are full')

        return value

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'sumit' and ct.lower() != 'lucknow':
            raise serializers.ValidationError('name not will be ranchi')
        return data


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'