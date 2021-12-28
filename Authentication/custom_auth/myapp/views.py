from rest_framework import authentication
from .models import Student
from .serializers import StudentSerializer
from  rest_framework import  viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .customauth import CustomAuthentication


#  It automatically handles all the actions such as : list(),retrieve(),create(),update(),partial_update(),destroy()
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated] 
    
    # username = Dhruvil 'for custom authentication':-
    # For Browsable API, write below line in the browser:
        # For GET and POST -->  http://127.0.0.1:8000/myapp/router/StudentAPI/?username=Dhruvil  
        # For PUT,DELETE --> http://127.0.0.1:8000/myapp/router/StudentAPI/1/?username=Dhruvil