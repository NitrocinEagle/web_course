# -*- coding: utf8 -*-
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from models import UserProfile


def get_cntxt_data(self, **kwargs):
    user = User.objects.get(username=self.request.user)
    context = super(self.__class__, self).get_context_data(**kwargs)
    context['user_profile'] = UserProfile.objects.get(user=user)
    return context


class UserProfileView(TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        return get_cntxt_data(self, **kwargs)


class AchievmentsView(TemplateView):
    template_name = 'user/achievments.html'

    def get_context_data(self, **kwargs):
        return get_cntxt_data(self, **kwargs)


class UserSettingsView(TemplateView):
    template_name = 'user/settings.html'

    def get_context_data(self, **kwargs):
        return get_cntxt_data(self, **kwargs)
