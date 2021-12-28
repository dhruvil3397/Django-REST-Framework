from re import I
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import BaseAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# NOTE : whenever we use function based authentication,we require 2 decorators.
# 1. authentication_classes     2. permission_classes 


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def studentdetail(request,pk = None):
    # Get the data
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        print(id) # it gives parsed data directly inside the request.data
        if id is not None:
            stu = Student.objects.get(id =id)
            # stu is complex data
            serializer = StudentSerializer(stu) # serializer converts complex to python
            print(serializer.data) # serializer.data is python data
            return Response(serializer.data)# it directly convert serialized data into json data and send the response
        # ELse it returns whole queryset
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        print(serializer.data)
        return Response(serializer.data)

    # Post the data
    if request.method == 'POST':
        # request.body gives json data
        # request.data gives python data 
        serializer = StudentSerializer(data = request.data)
        # serializer converts python data to complex data type
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            data = {'msg':'Data Created'}
            return Response(data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors)

    # Complete Update data
    if request.method == 'PUT':
        # id = request.data.get('id')
        stu = Student.objects.get(id = pk)
        # serializer converts python data to complex data type
        serializer = StudentSerializer(stu,data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            data = {'msg':'Data Completely Updated'}
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    # Partial Update data
    if request.method == 'PATCH':
        # id = request.data.get('id')
        stu = Student.objects.get(id = pk)
        # serializer convert complex data to python data
        serializer = StudentSerializer(stu,data = request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            data = {'msg':'Data Partialy Updated'}
            return Response(data)
        return Response(serializer.errors)
    
    # Delete the data
    if request.method == 'DELETE':
        # id = request.data.get('id')
        stu = Student.objects.get(id = pk)
        stu.delete()
        
        data = {'msg':'Data Deleted'}
        return Response(data)
       