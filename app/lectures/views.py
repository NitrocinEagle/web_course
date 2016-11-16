# -*- coding: utf8 -*-
from django.views.generic import ListView, TemplateView
from .models import Lecture


class LecturesView(ListView):
    template_name = 'lectures/index.html'
    model = Lecture
    context_object_name = 'lectures'


class LessonView(TemplateView):
    def get_template_names(self):
        return 'lectures/materials/lesson' + str(self.kwargs.get('lesson_num')) + '.html'
