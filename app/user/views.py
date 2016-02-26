# -*- coding: utf8 -*-
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from models import UserProfile


class UserProfileView(TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.request.user)
        context = super(UserProfileView, self).get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=user)
        context['user_profile'] = user_profile
        return context


class UserTasksView(TemplateView):
    template_name = 'user/tasks.html'

class AchievmentsView(TemplateView):
    template_name = 'user/achievments.html'