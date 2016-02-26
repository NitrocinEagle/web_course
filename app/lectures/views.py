# -*- coding: utf8 -*-
from django.views.generic import ListView
from models import Lecture


class LecturesView(ListView):
    template_name = 'lectures/index.html'
    model = Lecture
    context_object_name = 'lectures'
