from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id','url','name','roll','city']

        # Here, 'url' returns This Hyperlink
        #  "url": "http://127.0.0.1:8000/studentapi/1/"
        # This link provides particular user's data
        