from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    about = models.TextField(blank=True)