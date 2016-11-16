# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name='Название книги', max_length=128)
    author = models.CharField(verbose_name='Автор', max_length=128)
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % self.title


class LibraryAPISetting(models.Model):
    get_allowed = models.BooleanField(verbose_name='Разрешены get-методы', default=True)
    post_allowed = models.BooleanField(verbose_name='Разрешены post-методы', default=True)


class BookMark(models.Model):
    title = models.CharField(verbose_name='Название закладки', max_length=128)
    book_id = models.ForeignKey(Book, verbose_name='Книга')
    user_id = models.ForeignKey(User, verbose_name='Пользователь')
    comment = models.TextField(verbose_name='Комментарий', blank=True)

    def __str__(self):
        return '%s' % self.title
