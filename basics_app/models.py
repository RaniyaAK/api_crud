from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    name= models.CharField(max_length=100)
    age= models.PositiveIntegerField()
    place= models.CharField(max_length=100)
