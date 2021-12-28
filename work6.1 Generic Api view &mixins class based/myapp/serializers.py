from django.db import models
from rest_framework import fields, serializers

from .models import Student


# Model serializer has inbuilt create and update method,So we do not write externally:
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['id','name','roll','city']

    