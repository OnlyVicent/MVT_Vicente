from django.db import models

# Create your models here.

class Family_members(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField(null=True)
    alive = models.IntegerField(null=True)


