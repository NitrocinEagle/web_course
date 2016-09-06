# -*- coding: utf-8 -*-
from django.db import models


class FAQ(models.Model):
    class Meta:
        ordering = ['id']

    question = models.CharField(verbose_name=u'Вопрос', max_length=100)
    answer = models.CharField(verbose_name=u'Ответ', max_length=500)

    def __unicode__(self):
        return u'%s. %s' % (self.id, self.question)
