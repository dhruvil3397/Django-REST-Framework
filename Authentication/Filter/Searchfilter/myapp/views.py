from django.shortcuts import render
from myapp.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','city']
    # ^ symbol indicates that write only first letter of the name,yo will get filtered data
    #search_fields = ['^name']

    # = symbol indiactes ,to write exaxt name as in the data
    # search_fields = ['=name']
