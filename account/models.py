from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=16)

    def __str__(self):
        return self.email
