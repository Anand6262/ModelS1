from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name', 'roll', 'city']




#NO NEED TO WRITE BECAUSE WE ARE USING HERE ModelSerializer
# class StudentSerializer(serializers.Serializer):
#     id=serializers.IntegerField()    #NO NEED TO WRITE
#     name=serializers.CharField(max_length=255)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=255)

#     def create(self, validate_data):    #NO NEED TO WRITE BECAUSE WE ARE USING HERE ModelSerializer
#         return Student.objects.create(**validate_data)

#     def update(self, instance, validate_data):    #NO NEED TO WRITE BECAUSE WE ARE USING HERE ModelSerializer
#         instance.name= validate_data.get('name', instance.name)
#         instance.roll= validate_data.get('roll', instance.roll)
#         instance.city= validate_data.get('city', instance.city)
#         instance.save()
#         return instance