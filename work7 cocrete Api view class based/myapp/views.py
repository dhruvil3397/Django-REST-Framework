from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView, UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
#concreate Api view class method :
# Get the List of objects or Queryset:
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Create the new Model Instance:
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Update the update Model Instance:
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve the  Model Instance:
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Delete the  Model Instance:
class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# read queryset/create the  Model Instance:
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# read / delete the  Model Instance:
class StudentRD(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# read / update the  Model Instance:
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# read / update / delete the  Model Instance:
class StudentRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer