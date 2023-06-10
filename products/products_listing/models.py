from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    description = models.TextField()
    ean13 = models.CharField(max_length=13)
    units_number = models.PositiveIntegerField()
    dun14 = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.id}: {self.name}"
