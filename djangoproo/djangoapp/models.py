from django.db import models

# Create your models here.

class Data(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    msg=models.CharField(max_length=20)






















# class mytbl(models.Model):
#     name = models.TextField(max_length=50)
#     img = models.ImageField(upload_to='image/')
