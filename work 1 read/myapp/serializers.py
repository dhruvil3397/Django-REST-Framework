from rest_framework import serializers

# Create your serializers here.

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20)

