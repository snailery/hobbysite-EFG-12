from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=63)
    
    def __str__(self):
        return f"{self.user.pk}: {self.user.username} ({self.display_name})"

