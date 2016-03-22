# -*- coding: utf8 -*-
from django.conf.urls import url
from .views import NewsView, NewsPage

urlpatterns = [
    url(r'^(\d+)/$', NewsView.as_view()),
    url(r'^page/(\d+)/$', NewsPage.as_view()),
]
