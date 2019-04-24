from django.db import models

# Create your models here.
class bookdetails(models.Model):
    title=models.CharField(max_length=32)
    detail=models.CharField(max_length=200)
    imgs=models.CharField(max_length=200)