# -*- coding: utf8 -*-
from django.views.generic import TemplateView

class TimetableView(TemplateView):
    template_name = 'timetable/index.html'
