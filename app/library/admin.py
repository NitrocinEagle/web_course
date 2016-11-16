# -*- coding: utf8 -*-
from django.contrib import admin
from .models import Book, BookMark, LibraryAPISetting

admin.site.register(Book)
admin.site.register(LibraryAPISetting)
admin.site.register(BookMark)
