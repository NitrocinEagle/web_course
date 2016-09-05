# -*- coding: utf8 -*-
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, TemplateView
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm
from app.news.models import News


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "home/login.html"
    success_url = "/home"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/home")


class HomeCourseView(ListView):
    template_name = 'home/index.html'
    context_object_name = 'news'
    news_view_count = 2

    def get_queryset(self):
        return News.objects.all()[:self.news_view_count]
