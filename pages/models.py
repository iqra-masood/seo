from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name

    # You can add additional fields as needed
class Domain(models.Model):
    name = models.CharField(max_length=255)

class joinUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class joiners(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    domain = models.CharField(max_length=255)
    file = models.FileField(upload_to="data")
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
