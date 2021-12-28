from functools import partial
from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt

# This is read operations.
@csrf_exempt
def studentdetails(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print(python_data)
        id = python_data.get('id',None)
        if id is not None:
            # create model instance for one student
            stu =Student.objects.get(id = id)
            # convert complex data into python data
            serializer = StudentSerializer(stu) # we get python data in serializer 
            # convert python data into json data
            json_data = JSONRenderer().render(serializer.data)
            print(json_data)
            return HttpResponse(json_data,content_type = 'application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many =True)
        return JsonResponse(serializer.data,safe = False)
        
#  This is the create operations.
    

    if request.method == 'POST':
        json_data = request.body     #Store the request body
        print(json_data)
        # convert json_data into stream
        stream = io.BytesIO(json_data)
        print(stream)
        # convert stream into python_data  / parsed_data
        python_data = JSONParser().parse(stream)
        print(python_data)
        # convert python_data into complex_data
        # creating serializer object
        serializer = StudentSerializer(data = python_data)
        print(serializer)
        
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Inserted'}
            json_data = JSONRenderer().render(response)
            print(json_data)
            return HttpResponse(json_data,content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type= 'application/json')

#  This is the update operations.    
    if request.method == "PUT":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        # which model instance to update
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        # convert python_data to complex data
        # For complete update-dont use partial = True
        #    serializer = StudentSerializer(stu,data=python_data)

        # For partial update-use partial=True 
        serializer = StudentSerializer(stu,data=python_data,partial= True)  
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data updated!!!'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')

#  This is the delete operations.    
    if request.method =="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        response = {'msg':'Data deleted !!!'}
        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data,content_type = 'application/json')
    return HttpResponse("Thanks")
            

    
    

def studentlist(request):
    stu = Student.objects.all()  # create queryset
    serializer = StudentSerializer(stu,many= True)  # convert complex data into python data
    json_data = JSONRenderer().render(serializer.data)  # convert python data into json data
    print(json_data)
    return HttpResponse(json_data,content_type = 'application/json')  
 

 

  
