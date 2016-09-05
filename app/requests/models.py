# -*- coding: utf-8 -*-
from django.db import models


class Request(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(verbose_name=u'Имя', max_length=256)
    group = models.CharField(verbose_name=u'Группа', max_length=256)
    date = models.DateTimeField(verbose_name=u'Дата и время', auto_now=True)
    email = models.CharField(verbose_name=u'Почтовый адрес', max_length=60)
    social = models.CharField(verbose_name=u'Страница в соц. сетях',
                              max_length=60)

    def __unicode__(self):
        return u'%s. %s' % (self.name, self.group)
