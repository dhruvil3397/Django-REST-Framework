from rest_framework import authentication
from .models import Student
from .serializers import StudentSerializer
from  rest_framework import  viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import MyRateThrottle

#  It automatically handles all the actions such as : list(),retrieve(),create(),update(),partial_update(),destroy()
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly] 
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # throttle_classes = [AnonRateThrottle,MyRateThrottle]

# Assign different throttling rates for multiple classes:
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly] 
#     throttle_classes = [AnonRateThrottle,MyRateThrottle]

    
    
    
   