# -*- coding: utf8 -*-
from django.core.paginator import Paginator, InvalidPage
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import News


class NewsView(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        current_page = Paginator(News.objects.all(), 2)
        try:
            return current_page.page(self.args[0])
        except InvalidPage:
            raise Http404


class NewsPage(ListView):
    template_name = 'news/article.html'
    context_object_name = 'article'

    def get_queryset(self):
        return get_object_or_404(News, id=self.args[0])
