from rest_framework import authentication
from .models import Student
from .serializers import StudentSerializer
from  rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


#  It automatically handles all the actions such as : list(),retrieve(),create(),update(),partial_update(),destroy()
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # If user is not Authenticated ,then only Read the data
    # If user is Authenticated ,then make any CRUD operations
    permission_classes = [IsAuthenticatedOrReadOnly] 
   
