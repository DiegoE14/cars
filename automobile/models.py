from django.db import models

# Create your models here.

class Auto(models.Model):
    marca=models.CharField(max_length=150, null=False)
    modelo=models.IntegerField(null=False)
    color=models.CharField(max_length=100, null=False)
