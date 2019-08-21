# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    #just a random addition to see if i could create a user with a phone number
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.email
