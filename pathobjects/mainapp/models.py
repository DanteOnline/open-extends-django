from django.db import models


# Create your models here.
class FilePath(models.Model):
    path = models.CharField(max_length=64, unique=True)
