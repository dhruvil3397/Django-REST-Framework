# Generic API View and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# List and Create - pk not required:---------------------------------------------

class StudentListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Get the List of objects or Queryset:
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

# Create the new Model Instance:
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)



# Retrieve,Update and Delete - pk required:-----------------------------------------

class StudentRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve the  Model Instance:
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

# Update the  Model Instance:
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs) 

# Delete the  Model Instance:
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)