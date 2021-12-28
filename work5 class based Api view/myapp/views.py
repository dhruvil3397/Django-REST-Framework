from re import I
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.

class studentdetail(APIView):
    def get(self,request,pk= None,format= None):
        id = pk # request.data.get('id')
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
    def post(self,request,format= None):
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
    def put(self,request,pk = None,format= None):
        id = pk
        stu = Student.objects.get(id = id)
        # serializer converts python data to complex data type
        serializer = StudentSerializer(stu,data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            data = {'msg':'Data Completely Updated'}
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # Partial Update data
    def patch(self,request,pk = None,format= None):
        id = pk
        stu = Student.objects.get(id = id)
        # serializer convert complex data to python data
        serializer = StudentSerializer(stu,data = request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            data = {'msg':'Data Partialy Updated'}
            return Response(data)
        return Response(serializer.errors)
    
    # Delete the data
    def delete(self,request,pk = None,format= None):
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
        
        data = {'msg':'Data Deleted'}
        return Response(data)
       