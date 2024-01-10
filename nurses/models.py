from django.db import models

# Create your models here.

class Nurse(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name