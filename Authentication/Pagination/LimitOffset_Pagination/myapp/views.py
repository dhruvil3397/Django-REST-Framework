from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import pagination
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from .mypagination import MyLimitOffsetPagination

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Pagination for per view class:----------------------------------------------
    # Please see the bottom lines of code in settings.py to comment out global settings
    # For Pagination per view class: 1st create separate file -here mypagination.py for custom LimitOffsetPagination
    pagination_class = MyLimitOffsetPagination
    # pattern :---------http://127.0.0.1:8000/studentapi/?limit=4&offset=10
    # This pattern will return records from 11 to 14, because limit=4 and offset=10
