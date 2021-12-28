from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import pagination
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from .mypagination import MyCursorPagination

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    pagination_class = MyCursorPagination

