# -*- coding: utf8 -*-
from models import Book, BookMark, LibraryAPISetting
from django.contrib import admin

admin.site.register(Book)
admin.site.register(LibraryAPISetting)
admin.site.register(BookMark)
