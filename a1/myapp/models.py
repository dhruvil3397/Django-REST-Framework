from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',
                                blank=False, null=False)
    based_location = models.CharField(max_length=50, blank=True)
    is_available = models.BooleanField(default=False, blank=True)