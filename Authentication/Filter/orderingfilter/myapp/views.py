from django.shortcuts import render
from myapp.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]


    # This 'name' attribute ,order only by name
    # ordering_fields = ['name'] 
    