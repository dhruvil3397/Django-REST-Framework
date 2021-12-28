from rest_framework import authentication

from myapp.custompermission import MyPermission
from .models import Student
from .serializers import StudentSerializer
from  rest_framework import  viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermission import MyPermission

#  It automatically handles all the actions such as : list(),retrieve(),create(),update(),partial_update(),destroy()
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # For single class authentication as described below:
    authentication_classes = [SessionAuthentication] 
    # AllowAny : Access all authenticated and unauthenticated users
    #permission_classes = [AllowAny] 

    # IsAuthenticated : Only Authenticated users access it
    #permission_classes = [IsAuthenticated]

    # IsAdminUser : Only staff user is True access it
    #permission_classes = [IsAdminUser]

    # IsAuthenticatedOrReadOnly : Authenticated users have all access,but Unauthenticated users have Read access
    #permission_classes = [IsAuthenticatedOrReadOnly]

    # DjangoModelPermissions : Authenticated users have predefined permissions,but Unauthenticated users dont have Read access
    #permission_classes = [DjangoModelPermissions]

    # DjangoModelPermissionsOrAnonReadOnly : Authenticated users have predefined permissions,but Unauthenticated users have only Read access
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    # Custom Permission:
    permission_classes = [MyPermission]

    
    # Similarly, For more than one class , follow the bottom lines of the settings.py
