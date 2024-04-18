from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    add=models.CharField(max_length=120)


    def __str__(self):
        return self.email
    

class SignUp(models.Model):
    email = models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    username=models.CharField(max_length=120)


    def __str__(self):
        return self.username