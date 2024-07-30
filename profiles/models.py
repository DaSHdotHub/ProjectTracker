from django.db import models
from django.contrib.auth.models import User

"""
Profile model with data fields for bio and profile_picture
"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
