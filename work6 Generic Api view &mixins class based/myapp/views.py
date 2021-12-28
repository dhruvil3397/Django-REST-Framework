# Generic API View and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Get the List of objects or Queryset:
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

# Create the new Model Instance:
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

# Retrieve the new Model Instance:
class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

# Update the  Model Instance:
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)


# Delete the  Model Instance:
class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)