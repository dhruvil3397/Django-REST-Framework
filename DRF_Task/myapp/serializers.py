from django.db import models
from rest_framework import fields, serializers

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from myapp.models import UserProfile


# Model serializer has inbuilt create and update method,So we do not write externally:
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields =['id','username','email','first_name','last_name']
        read_only_fields = ['username']  # It does not change the username,also we don't required to pass the username for update data

class UserProfileSerializer(serializers.ModelSerializer):
   
    class Meta:

        model = UserProfile
        fields = ['phone','birthdate','permission','image']


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields =['key']


    