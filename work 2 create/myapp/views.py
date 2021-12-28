from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from.serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def studentcreate(request):
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
            return HttpResponse(json_data,content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type= 'application/json')
    return HttpResponse('Thank you')


    
