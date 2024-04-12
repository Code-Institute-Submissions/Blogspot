from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Mask sensitive fields before saving
        self.password = '*' * len(self.password)
        super().save(*args, **kwargs)