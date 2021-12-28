from rest_framework import serializers

from myapp.models import Student


class StudentSerializer(serializers.Serializer):
   
    name = serializers.CharField(max_length=20)
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