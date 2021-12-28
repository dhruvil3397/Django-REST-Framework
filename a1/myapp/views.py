from .models import Profile, User
from .serializers import UserSerializer,ProfileSerializer
from  rest_framework import  serializers, viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@csrf_exempt
@api_view(['GET','PUT','POST'])  
def home(request):
    
    if request.method =='PUT':
        id = request.data.get('id',None)
        print(id)
        user_obj = User.objects.get(id=id)
        print(user_obj)
        user_serializer = UserSerializer(user_obj,data = request.data)

        profile_obj = Profile.objects.get(user_id=id)
        profile_serializer = ProfileSerializer(profile_obj,data=request.data)
        
      
        if user_serializer.is_valid() and profile_serializer.is_valid():
            user_serializer.save()
            profile_serializer.save()
            data = {'msg':'Data Updated'}
            return Response(data,status = status.HTTP_201_CREATED)
        return Response(profile_serializer.errors)
    return Response({'msg':'ok'})