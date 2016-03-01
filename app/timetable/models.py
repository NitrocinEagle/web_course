# -*- coding: utf8 -*-
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=128)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name
