# -*- coding: utf8 -*-
from django.db import models


class Lecture(models.Model):
    topic = models.CharField(max_length=128)
    about = models.TextField()

    def __unicode__(self):
        return u'%s. %s' % (self.id, self.topic)
