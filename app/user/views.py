# -*- coding: utf8 -*-
from django.views.generic import TemplateView


class UserProfileView(TemplateView):
    template_name = 'user/profile.html'


class UserTasksView(TemplateView):
    template_name = 'user/tasks.html'
