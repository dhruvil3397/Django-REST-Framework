from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender =models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer,on_delete=CASCADE,related_name='song')
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
