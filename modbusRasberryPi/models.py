from django.db import models

# Create your models here.
class Digital (models.Model):
    coil_value =models.BooleanField(default=False)
        
class Analog (models.Model):
    register_value =models.IntegerField(default=0)