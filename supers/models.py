from tokenize import Name
from unicodedata import name
from django.db import models

# Create your models here.
class Super(models.Model):
    name : models.CharField(max_length=255)
    alter_ego : models.CharField(max_length=255)
    primary_ability : models.CharField(max_length=255)
    secondary_ability : models.CharField(max_length=255)
    catchprase : models.CharField(max_length=255)
    super_type : models.ForeignKey(Super_Types, on_delete=models.CASCADE)