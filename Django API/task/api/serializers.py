from django.db import models
from django.db.models import fields
from task.models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta :
        model = Contact
        fields = ['id','name','email','phone','message']