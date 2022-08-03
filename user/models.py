from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=50)



class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    molile_number=models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL,blank=True,null=True)






