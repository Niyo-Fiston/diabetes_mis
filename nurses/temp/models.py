# nurses/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# CustomUser model extending AbstractUser
class CustomUser(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# Nurse model with a one-to-one relationship with CustomUser
class Nurse(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Admin model with a one-to-one relationship with CustomUser
class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add any additional fields relevant to the Admin model

    def __str__(self):
        return self.user.username
