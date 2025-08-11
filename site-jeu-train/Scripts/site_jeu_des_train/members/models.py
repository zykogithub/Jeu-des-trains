from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
  station = models.CharField(max_length=255)
  lignes = models.CharField(max_length=255)
  nombre_de_passagers = models.IntegerField(null=True)