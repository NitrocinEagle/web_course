# -*- coding: utf8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Book, LibraryAPISetting


class SelectBooks(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        if not LibraryAPISetting.objects.first().get_allowed:
            return Response({
                'result': 'error',
                'code': 2
            })
        try:
            books = Book.objects.all()
        except:
            return Response({
                'result': 'error',
                'code': 1
            })
        books_response = []
        for book in books:
            books_response.append(
                {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'price': book.price,
                    'description': book.description
                }
            )
        return Response(books_response)


class SetBook(APIView):
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        if not LibraryAPISetting.objects.first().post_allowed:
            return Response({
                'result': 'error',
                'code': 3
            })
        book = self.request.data
        try:
            book = Book.objects.filter(id=book.get('id'))
            if book:
                book.update(**book)
                return Response({
                    'result': 'success',
                    'code': 101,
                    'message': u'Book with id %s has been updated' % (book['id'])
                })
            else:
                new_book = Book(**book).save()
                return Response({
                    'result': 'success',
                    'code': 102,
                    'message': u'Book with id %s has been created' % (new_book.id),
                    'data': {
                        'id': new_book.id
                    }
                })
        except:
            return Response({
                'result': 'error',
                'code': 103
            })


class DeleteBook(APIView):
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        if not LibraryAPISetting.objects.first().post_allowed:
            return Response({
                'result': 'error',
                'code': 3
            })
        book = self.request.data
        try:
            Book.objects.filter(id=book.get['id']).delete()
            return Response({
                'result': 'success',
                'code': 104,
                'message': u'Book with id %s has been deleted' % (book.get['id']),
                'data': {
                    'id': book.get['id']
                }
            })
        except:
            return Response({
                'result': 'error',
                'code': 105
            })
