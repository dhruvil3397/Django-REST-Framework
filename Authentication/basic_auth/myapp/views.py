from rest_framework import authentication
from .models import Student
from .serializers import StudentSerializer
from  rest_framework import  viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


#  It automatically handles all the actions such as : list(),retrieve(),create(),update(),partial_update(),destroy()
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # For single class authentication as described below:
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]
    
    # Similarly, For more than one class , follow the bottom lines of the settings.py
