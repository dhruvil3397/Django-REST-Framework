from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView, UpdateAPIView,RetrieveAPIView,DestroyAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.throttling import ScopedRateThrottle

# Create your views here.
#concreate Api view class method :
# Get the List of objects or Queryset:
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

# Create the new Model Instance:
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

# Update the update Model Instance:
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'
    

# Retrieve the  Model Instance:
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

# Delete the  Model Instance:
class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'
