# -*- coding: utf8 -*-
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm


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
        return HttpResponseRedirect("/")


class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
