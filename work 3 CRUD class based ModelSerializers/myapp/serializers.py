from django.db.models import fields
from rest_framework import serializers, validators

from myapp.models import Student




        
class StudentSerializer(serializers.ModelSerializer):
    # Read_only :For single-field use below code:
    #name = serializers.CharField(read_only = True)
    # It does not update old name with the new name

    # Validators
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')
    name = serializers.CharField(validators= [starts_with_r] )
        
    class Meta :
        model = Student
        fields = ['name','roll','city']
        #read_only_fields = ['name','roll'] # Read_only : Use for Multiple-fields
        # Read_only : Or this way :
        #extra_kwargs = {'name':{'read_only':True}} 
    
    # field-level validation:
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value
        
    # Object-level validation:
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        print(nm,ct)
        if nm.lower() == "jack" and ct.lower() != "london":
            raise serializers.ValidationError('City must be London')
        return data
