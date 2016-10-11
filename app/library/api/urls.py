# -*- coding: utf8 -*-
from django.conf.urls import url
from .views import SelectBooks, SetBook, DeleteBook

urlpatterns = [
    url(r'^get_books/$', SelectBooks.as_view(), name='select_books'),
    url(r'^set_book/$', SetBook.as_view(), name='set_book'),
    url(r'^del_book/$', DeleteBook.as_view(), name='delete_book'),
]
