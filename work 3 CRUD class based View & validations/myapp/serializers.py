from rest_framework import serializers

from myapp.models import Student

# Validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should be start with R')
    

class StudentSerializer(serializers.Serializer):
   
    name = serializers.CharField(max_length=20,validators =[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20)


    # This is create the new model object create method
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # This is update the old model object update method
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

    
    # field-level validation:
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # Object-level validation:
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        print(nm,ct)
        if nm.lower() == "dhruvil" and ct.lower() != "ahmedabad":
            raise serializers.ValidationError('City must be Ahmedabad')
        return data