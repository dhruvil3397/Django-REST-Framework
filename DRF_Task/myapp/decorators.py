from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http.response import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import UserProfile
import io
from rest_framework.parsers import JSONParser
from .serializers import TokenSerializer
import requests
from functools import wraps


# Argument based custom decorator :------------------------
# (*param) is these arguments ('Admin','Uploader','Editor')
def user_is_entry_author(*param):
    def decorator(view_func): # Here, view_func is an object and it calls  the def edit(request): in views.py
                            # OR view_func is an edit function of views.py
        # NOTE : creating any decorator function,you need wrap function
        def wrap(request, *args, **kwargs): # Here it accepts all the arguments,which accepts view_func
            try :
                print(view_func)
                token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
                print(token)
                user_id = Token.objects.get(key=token).user_id
                print(user_id)
                user = User.objects.get(id=user_id)
                print(user)
                profile = UserProfile.objects.filter(user=user,permission__in= [*param]).exists()
                print(profile)    
                if profile == True:
                    return view_func(request, *args, **kwargs)
                else :
                    return JsonResponse({'msg':'Invalid token or Permission Denied'})
          
            except:
                return JsonResponse({'msg':'Invalid token or Permission Denied'})

        return wrap
    return decorator