from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from  rest_framework import  viewsets
from rest_framework import status

class StudentViewSet(viewsets.ViewSet):
    # Get the List of objects or Queryset
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many= True)
        return Response(serializer.data)

    # Create the new Model Instance:
    def create(self,request):
        # request.data gives python data and request.body gives json data
        serializer= StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    # Retrieve the  Model Instance:
    def retrieve(self,request,pk = None):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu)    # convert complex data to python data
        return Response(serializer.data)   # Here Response convert python to json data

    # Complete update the model instance
    def update(self,request,pk = None):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Completely Updated'},status = status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    # Partial update the model instance
    def partial_update(self,request,pk = None):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Partially Updated'},status = status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    # Delete the model instance
    def destroy(self,request,pk = None):
        stu = Student.objects.get(pk = None)
        stu.delete()
        return Response({'msg':'Successfully Deleted'})        