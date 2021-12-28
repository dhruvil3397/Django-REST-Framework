from django.db import models
from django.contrib.auth.models import Permission, User
from django.db.models.deletion import CASCADE

# Create your models here.
choice = (('Admin','Admin'),
            ('Editor','Editor'),
            ('Uploader','Uploader'))
class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=CASCADE)
    phone = models.IntegerField(blank=True,null=True)
    birthdate =models.DateField(blank=True,null=True)
    image = models.ImageField(upload_to = 'myapp/images')
    permission = models.CharField(max_length=100,choices= choice)
    
    def __str__(self) -> str:
        return self.permission


