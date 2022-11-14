from django.db import models

# Create your models here.
class Super_Types(models.Model):
    type_of_super = models.CharField(max_length=255)
    