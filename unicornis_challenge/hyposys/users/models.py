# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    """Custom User model for application in the hyposys app.

    Builds off the already implemented Django User as per reccomendation in the
    Django `documentation <https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project>`_.
    TODO: write documentation properly.

    Attrs:
    """
    pass
