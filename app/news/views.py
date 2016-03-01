    # -*- coding: utf8 -*-
from django.views.generic import ListView
from models import News


class NewsView(ListView):
    template_name = 'news/index.html'
    model = News
    context_object_name = 'news'
