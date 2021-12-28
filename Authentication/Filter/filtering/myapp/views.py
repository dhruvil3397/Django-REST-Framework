from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers

from myapp.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView



# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Method overriding:
    #Any user login in django-admin,they will come below
    # This method filter the login user data
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)
