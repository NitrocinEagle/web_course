# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    group = models.CharField(blank=True, max_length=8)
    sub_group = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    date_joined = models.DateField()
    about = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name
