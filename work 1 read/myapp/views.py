from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
# Model object -single student data

def student_details(request,pk):
    # Create model instance/object for one student
    stu = Student.objects.get(id=pk) # This is complex data-type
    print(stu)
    print("----------------------")
    serializer = StudentSerializer(stu)  # Convert complex data-type into python data-type such as in dictionary form
    print(serializer)
    print(serializer.data)
    print("----------------------")
    # There are two ways to covert serialized data into json data
    # This is the first way as below and second way in the next method def student_list(request):
    json_data = JSONRenderer().render((serializer.data)) # Convert serialized_data/python data-type into json_data
    print(json_data)
    return HttpResponse(json_data,content_type = 'application/json') # Transfer the json_data to the client

# Query set - All Student data :

def student_list(request):
    # Create create query set
    stu = Student.objects.all() # This is complex data-type
    print(stu)
    print("----------------------")
    serializer = StudentSerializer(stu,many = True )  # Convert complex data-type into python data-type such as in dictionary form
    print(serializer)
    print(serializer.data)
    print("----------------------")
    # This is the second short way to both convert the data into json and transfer the json_data to the client in one line of code as below:
    return JsonResponse(serializer.data,safe=False) 
    # Here safe= False,because we pass query set to the JsonResponse and that query set is in list of dict form.
