# -*- coding: utf8 -*-
from django.views.generic import TemplateView
from models import UserProfile


class UserViewBase(TemplateView):
    template_name = 'empty'

    def get_context_data(self, **kwargs):
        kwargs['user_profile'] = UserProfile.objects.get(user=self.request.user)
        return super(UserViewBase, self).get_context_data(**kwargs)


class UserProfileView(UserViewBase):
    template_name = 'user/profile.html'


class AchievmentsView(UserViewBase):
    template_name = 'user/achievments.html'


class UserSettingsView(UserViewBase):
    template_name = 'user/settings.html'
