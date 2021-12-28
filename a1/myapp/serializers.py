from rest_framework import serializers
from django.contrib.auth.models import User

from myapp.models import Profile


class UserSerializer(serializers.ModelSerializer):
      
    class Meta:

        model = User
        fields = ['id','username','first_name', 'last_name']
        read_only_fields = ['username']
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = Profile
        fields = ['based_location', 'is_available']