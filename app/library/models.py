# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(verbose_name=u'Название книги', max_length=128)
    author = models.CharField(verbose_name=u'Автор', max_length=128)
    price = models.FloatField(verbose_name=u'Цена')
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.title


class LibraryAPISetting(models.Model):
    get_allowed = models.BooleanField(verbose_name=u'Разрешены get-методы', default=True)
    post_allowed = models.BooleanField(verbose_name=u'Разрешены post-методы', default=True)


class BookMark(models.Model):
	title = models.CharField(verbose_name=u'Название закладки', max_length=128)
	book_id = models.ManyToOneRel(Book, verbose_name=u'Книга', max_length=128)
	user_id = models.ManyToOneRel(User, verbose_name=u'Пользователь', max_length=128)
	comment = models.TextField(verbose_name=u'Комментарий', blank=True)

	def __unicode__(self):
        return u'%s' % self.title