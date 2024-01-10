from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    glucose_level = models.FloatField()
    treatment_plan = models.TextField()
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"