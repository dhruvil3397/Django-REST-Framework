from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import pagination
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from .mypagination import MyPageNumberPagination

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Pagination for per view class:----------------------------------------------
    # Please see the bottom lines of code in settings.py to comment out global settings
    # For Pagination per view class: 1st create separate file -here mypagination.py for custom PageNumberPagination
    pagination_class = MyPageNumberPagination
