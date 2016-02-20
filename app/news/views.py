# -*- coding: utf8 -*-
from django.views.generic import TemplateView


class NewsView(TemplateView):
    template_name = 'news/index.html'