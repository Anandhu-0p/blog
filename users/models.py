
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.username
